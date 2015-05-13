from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'webapps.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'socialnetwork.views.welcome', name='home'),
    url(r'^regNewUser$', 'socialnetwork.views.registerNewUser'),
    url(r'^stream/$', 'socialnetwork.views.stream'),
    url(r'^login$', 'django.contrib.auth.views.login', {'template_name':'socialnetwork/login.html'}))

