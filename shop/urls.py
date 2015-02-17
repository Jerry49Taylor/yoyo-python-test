from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from views import CustomerDetail, CustomerList, ProductDetail, ProductList, StampList, TransactionDetail, TransactionList, TransactionLineDetail, TransactionLineList, VoucherDetail, VoucherList


urlpatterns = [
    url(r'^customers/$', CustomerList.as_view()),
    url(r'^customers/(?P<pk>[0-9]+)/$', CustomerDetail.as_view()),
    url(r'^products/$', ProductList.as_view()),
    url(r'^products/(?P<pk>[0-9]+)/$', ProductDetail.as_view()),
    url(r'^stamps/$', StampList.as_view()),
    url(r'^transactions/$', TransactionList.as_view()),
    url(r'^transactions/(?P<pk>[0-9]+)/$', TransactionDetail.as_view()),
    url(r'^transactionlines/$', TransactionLineList.as_view()),
    url(r'^transactionlines/(?P<pk>[0-9]+)/$', TransactionLineDetail.as_view()),
    url(r'^vouchers/$', VoucherList.as_view()),
    url(r'^vouchers/(?P<pk>[0-9]+)/$', VoucherDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
