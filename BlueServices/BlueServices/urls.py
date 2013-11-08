from django.conf.urls import patterns, include, url
from BlueServices.Login import views
#from Login.resource import login

#log = login()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'BlueServices.views.home', name='home'),
    # url(r'^BlueServices/', include('BlueServices.BlueServices.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^$', views.index, name='index'),
    url(r'^user/login/', views.login, name='login'),
    #url(r'^api/', include(my.urls))
)
