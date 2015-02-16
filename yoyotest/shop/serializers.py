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


class TransactionLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionLine
        fields = ('id', 'transaction', 'product', 'quantity')
        read_only_fields = ('id')


class TransactionSerializer(serializers.ModelSerializer):
    transactionlines = TransactionLineSerializer(many=True, read_only=True)

    class Meta:
        model = Transaction
        fields = ('id', 'customer', 'date_created', 'transactionlines')
        read_only_fields = ('id', 'date_created', 'transactionlines')
