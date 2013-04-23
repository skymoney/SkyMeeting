'''
Created on 2013-4-23

Settings file for production

@author: cheng
'''
from settings import *

DEBUG = TEMPLATE_DEBUG = False

ADMINS = (
    #('Your Name', 'your_email@example.com'),
    ('Cheng,Qian','qc09@software.nju.edu.cn'),
)

ALLOWED_HOSTS = '*'

TIME_ZONE = 'Asia/Shanghai'
