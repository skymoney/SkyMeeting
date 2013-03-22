from django.conf.urls import patterns, include, url
from django.conf import settings
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns=patterns('MemManage.views',
    url(r'^members/$','member'),
    url(r'^members/edituser','editRoleInfo'),
    url(r'^members/addgroup/$','addGroup'),
    url(r'^members/addtag/$','addTag'),
)

urlpatterns += patterns('',
    # Examples:
    # url(r'^$', 'SkyMeeting.views.home', name='home'),
    # url(r'^SkyMeeting/', include('SkyMeeting.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^public/(?P<path>.*)$','django.views.static.serve',{"document_root":settings.STATIC_PATH}), #add static files
    url(r'^$','Login.views.welcome'),
    url(r'^login/$','Login.views.login'),  
    url(r'^logout/$','Login.views.logout'),
    url(r'^home/$','Login.views.home'),
    url(r'^boards/$','Meeting.views.boards'),    
    url(r'^meetings/$','Meeting.views.meetings'),
    url(r'^documents/$','Meeting.views.documents'),
    url(r'^newmeeting/$','Meeting.views.newMeeting'),
)
