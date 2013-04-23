from django.conf.urls import patterns, include, url
from django.conf import settings
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('Login.views',
    url(r'^$','welcome'),
    url(r'^login/$','login'),  
    url(r'^logout/$','logout'),
    url(r'^home/$','home'),
    url(r'^invite/$','invite'),
    url(r'^register/$','register'),
    url(r'^registernewaccount/$','registerNewAccount'),
    url(r'^resetpassword/$','resetPassword'),
)

urlpatterns += patterns('General.views',
    url(r'^dashboard/$','dashboard'),
    url(r'^setrole/$','changeCurRid'),
    url(r'^profile/$','profile'),
    url(r'^editprofile/$','editProfile'),
    url(r'^editaccount/$','editAccount'),
    url(r'^documents/$','documents'),
    url(r'^error/$','error'),
)

urlpatterns += patterns('MemManage.views',
    url(r'^members/$','members'),
    url(r'^members/edituser','editRoleInfo'),
    url(r'^members/inviteuser/$','inviteUser'),
    url(r'^members/deleteuser/$','deleteUser'),
    url(r'^members/addgroup/$','addGroup'),
    url(r'^members/editgroup/$','editGroup'),
    url(r'^members/deletegroup/$','deleteGroup'),
    url(r'^members/addtag/$','addTag'),
    url(r'^members/deletetag/$','deleteTag'),
    url(r'^members/queryperson/$','queryPerson'),
)

urlpatterns += patterns('Meeting.views',
    url(r'^meetings/$','meetings'),
    url(r'^newmeeting/$','newMeeting'),
    url(r'^savemeeting/$','saveMeeting'),
    url(r'^editmeeting/$','editMeeting'),
    url(r'^deletemeeting/$','deleteMeeting'),
    url(r'^meeting/$','meeting'),
    url(r'^meeting/addcomment/$','addComment'),
    url(r'^meeting/changestatus/$','changeStatus'),
    url(r'^upfile/$','uploadFile'),
    url(r'^downfile/$','downloadFile'),
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
    url(r'^setlang/$','django.views.i18n.set_language'),
    url(r'^jsi18n/(?P<packages>\S+)/$','django.views.i18n.javascript_catalog'),
)
