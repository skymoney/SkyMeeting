# Create your views here.

from django.shortcuts import render_to_response
from django.http import HttpResponse

import pymongo
import nltk
import re
import simplejson as json
from django.core.cache import cache

tagger=None

def amazon(request):
    tagger=nltk.data.load(nltk.tag._POS_TAGGER)    
    cache.set('tagger',tagger,3600)
    
    return render_to_response('amazon.html')

def get_from_sql(product_asin=None):
    #product id in mongodb        
    con=pymongo.Connection('192.168.100.229',27017)
    commodity_col=con['amazon_data']['commodity']   #get collection of target data
    comment_data=commodity_col.find_one({'ASIN':product_asin},{'_id':0,'comment':1})
    comment_content=comment_data['comment']
    return list(comment['Content'] for comment in comment_content)

def generate_key_word(all_data):
    #generate key words
    #currently simply use words frequent
    #not much nlp analysis
    total_content=[]
    stop_words=nltk.corpus.stopwords.words('english')
    pattern=re.compile(r'^[\w]*$')
    filter_set=['NN','NNP','NNS','JJ']  #filter noun and adjective
    
    for data in all_data:
        tagged_content=cache.get('tagger').tag(nltk.word_tokenize(data))
        for word in tagged_content:
            if re.match(pattern,word[0]) and word[0].lower() not in stop_words and word[1] in filter_set:
                total_content.append(word[0].lower())
    #clean dirty words
    fre_dict=dict()
    for word in total_content:
        fre_dict[word]=fre_dict[word]+1 if word in fre_dict.keys() else 1
    
    return fre_dict    

def get_index(data):
    #generate index for proper data size
    return data.index(min(data))

def get_des_from_sql(product_asin=None):
    #get description from mongo given product asin
    con=pymongo.Connection('192.168.100.229',27017)
    commodity_col=con['amazon_data']['commodity']   #get collection of target data
    des_data=commodity_col.find_one({'ASIN':product_asin},{'_id':0,'comment':0})
    feature=des_data['ProductInfo']['Feature']  #list type['','']
    description=des_data['ProductInfo']['Product Description']
    return list(data for data in feature)+list([description])

def generate(request):
    data=get_from_sql('B000CRH4FK')
    origin_dict=generate_key_word(data)
    kw_dict=sorted(origin_dict.iteritems(),key=lambda d:d[1],reverse=True)
    print kw_dict
    #index=get_index(list(data[1] for data in kw_dict))
    max_num=(float)(max(origin_dict.values()))  #get max number of weigh values to normalize
    return HttpResponse(json.dumps(list({'name':data[0],'weight':"%.3f"%(data[1]/max_num)} for data in kw_dict)))