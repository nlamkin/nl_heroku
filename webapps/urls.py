from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'webapps.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'regTheaterLocator.views.login', name ='home'),
    url(r'^index$', 'regTheaterLocator.views.index'),
    url(r'^list$', 'regTheaterLocator.views.list'),
    url(r'^results$', 'regTheaterLocator.views.showSearch'),
    url(r'^search$', 'regTheaterLocator.views.theaterSearch'),
    url(r'^manage$', 'regTheaterLocator.views.manageTheaters'),
    url(r'^manageShow$', 'regTheaterLocator.views.manageShow', name='manageShow'),
    url(r'^createTheater$', 'regTheaterLocator.views.createTheater',  name='createTheater'),
    url(r'^createProd$', 'regTheaterLocator.views.createProd',  name='createProd'),
    url(r'^editProfile/(\d+)$', 'regTheaterLocator.views.editProfile', name='editProfile'),    
    url(r'^register$', 'regTheaterLocator.views.register', name='register'),
    # Route for built-in authentication with our own custom login page
    url(r'^login$', 'django.contrib.auth.views.login', {'template_name':'regTheaterLocator/login.html'}, name='login'),
    # Route to logout a user and send them back to the login page
    
    url(r'^logout$', 'django.contrib.auth.views.logout_then_login'),
)