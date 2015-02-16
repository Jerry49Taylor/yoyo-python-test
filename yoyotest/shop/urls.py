from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from views import CustomerDetail, CustomerList, ProductDetail, ProductList, TransactionDetail, TransactionList, TransactionLineDetail, TransactionLineList


urlpatterns = [
    url(r'^customers/$', CustomerList.as_view()),
    url(r'^customers/(?P<pk>[0-9]+)/$', CustomerDetail.as_view()),
    url(r'^products/$', ProductList.as_view()),
    url(r'^products/(?P<pk>[0-9]+)/$', ProductDetail.as_view()),
    url(r'^transactions/$', TransactionList.as_view()),
    url(r'^transactions/(?P<pk>[0-9]+)/$', TransactionDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
