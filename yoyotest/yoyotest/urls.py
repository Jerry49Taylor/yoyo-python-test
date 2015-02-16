from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'yoyotest.views.home', name='home'),
    url(r'^shop/', include('shop.urls', namespace="shop")), 
    url(r'^docs/', include('rest_framework_swagger.urls')),  
    url(r'^admin/', include(admin.site.urls)),
)
