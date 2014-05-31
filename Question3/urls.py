from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.views.generic import TemplateView
from Question3 import settings
from file_upload.views import Signup, Login, FileUploadView

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Question3.views.home', name='home'),
    # url(r'^Question3/', include('Question3.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^register/$',Signup.as_view()),
    url(r'^signin/$',Login.as_view()),
    url(r'^upload-file/$',FileUploadView.as_view()),

    url(r'^logout/$', 'file_upload.views.logout_user', name='logout'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
    #url(r'^show/$',TemplateView.as_view(template_name='signup.html')),
)

