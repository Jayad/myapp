from django.conf.urls import patterns, include, url

#from django.contrib import admin
#admin.autodiscover()

#urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

 #   url(r'^admin/', include(admin.site.urls)),
#)


from django.conf.urls import patterns, include, url
from login.views import *
 
urlpatterns = patterns('',
    url(r'^$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', logout_page),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'), # If user is not login it will redirect to login page
    url(r'^register/$', register),
    url(r'^register/success/$', register_success),
    url(r'^home/$', home),
)
