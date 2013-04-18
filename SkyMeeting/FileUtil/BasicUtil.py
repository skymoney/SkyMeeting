#-*- coding:utf-8 -*-
'''
Created on 2013-4-17

@author: cheng
'''
from django.http import HttpResponse
from Meeting.models import File

def downloadFile(params):
    '''
    download select file,currently very big file not considered
    @param fid: id of file to be downloaded 
    '''
    fobj=File.objects.get(file_id=params["fid"])
    f=open(fobj.file_path,'rb')
    fdata=f.read()
    f.close()
    
    response=HttpResponse(fdata,mimetype='application/octet-stream')
    response["Content-Disposition"]='attachment;filename=%s'%fobj.file_name
    
    return response
