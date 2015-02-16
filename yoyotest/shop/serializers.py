'''
Created on 16 Feb 2015

@author: jeremy
'''

from rest_framework import serializers

from models import Customer, Product, Transaction, TransactionLine


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'first_name', 'last_name', 'balance', 'unredeemed_vouchers')
        read_only_fields = ('balance', 'unredeemed_vouchers')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'sku', 'stamps_earned')
        read_only_fields = ('sku', 'stamps_earned')


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('id', 'customer', 'date_created')
        read_only_fields = ('customer', 'date_created')


class TransactionLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionLine
        fields = ('id', 'product', 'quantity')
        read_only_fields = ('product', 'quantity')
