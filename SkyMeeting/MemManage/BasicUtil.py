#-*-coding:utf-8-*-

'''
Description: Provide basic ops for views methods

Created on 2013-3-23

@author: cheng

@contact: CChain0615@gmail.com
'''

def listToInt(slist):
    numList=[]
    for s in slist:
        num=int(s)
        numList.append(num)
    return numList