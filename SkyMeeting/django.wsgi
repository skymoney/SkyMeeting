import os
import sys
import django.core.handlers.wsgi
sys.path.append(r'/home/cheng/Workspace/git/SkyMeeting')
os.environ['DJANGO_SETTINGS_MODULE'] = 'SkyMeeting.settings'
application = django.core.handlers.wsgi.WSGIHandler()
