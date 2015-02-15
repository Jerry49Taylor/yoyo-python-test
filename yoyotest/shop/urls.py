from django.conf.urls import patterns, url
from . import views 

urlpatterns = patterns('shop.views',
    url(r'^get_stamp_count/(?P<customer_id>\d+)/$', views.get_stamp_count, name='get_stamp_count'),
)
