import os
import sys
import django.core.handlers.wsgi
sys.path.append('/home/cheng/Workspace/git/SkyMeeting')
sys.path.append('/home/cheng/Workspace/git/SkyMeeting/SkyMeeting')
os.environ['DJANGO_SETTINGS_MODULE'] = 'SkyMeeting.settings'
os.environ['PYTHON_EGG_CACHE']='/tmp'
application = django.core.handlers.wsgi.WSGIHandler()
print >> sys.stderr,sys.path
