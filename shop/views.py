import json

from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST, require_GET

from models import Customer, Product, Transaction, TransactionLine, Stamp, Voucher
from serializers import CustomerSerializer, ProductSerializer, StampSerializer, TransactionSerializer, TransactionLineSerializer, VoucherSerializer
from rest_framework import generics


class CustomerList(generics.ListCreateAPIView):
    """
    List all Customers or Create a new Customer
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Read, Update or Delete a Customer instance
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class ProductList(generics.ListCreateAPIView):
    """
    List all Products or Create a new Product
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Read, Update or Delete a Product instance
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class StampList(generics.ListCreateAPIView):
    """
    List all Stamps or Create a new Stamp
    """
    queryset = Stamp.objects.all()
    serializer_class = StampSerializer


class TransactionList(generics.ListCreateAPIView):
    """
    List all Transaction or Create a new Transaction
    """
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class TransactionDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Read, Update or Delete a Transaction instance
    """
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class TransactionLineList(generics.ListCreateAPIView):
    """
    List all Transaction or Create a new TransactionLine
    """
    queryset = TransactionLine.objects.all()
    serializer_class = TransactionLineSerializer


class TransactionLineDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Read, Update or Delete a TransactionLine instance
    """
    queryset = TransactionLine.objects.all()
    serializer_class = TransactionLineSerializer


class VoucherList(generics.ListCreateAPIView):
    """
    List all Vouchers or Create a new Voucher
    """
    queryset = Voucher.objects.all()
    serializer_class = VoucherSerializer


class VoucherDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Read, Update or Delete a Voucher instance
    """
    queryset = Voucher.objects.all()
    serializer_class = VoucherSerializer
