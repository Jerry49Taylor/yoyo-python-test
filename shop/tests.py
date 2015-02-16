
import json

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase

from models import Customer, Product, Stamp, Transaction, TransactionLine, Voucher


class TestTransaction(TestCase):

    def setUp(self):
        TestCase.setUp(self)
        self.customer = Customer.objects.create()
        self.widget = Product.objects.create(sku='widget', stamps_earned=1)

    def tearDown(self):
        Voucher.objects.all().delete()
        Stamp.objects.all().delete()
        TransactionLine.objects.all().delete()
        Transaction.objects.all().delete()
        Product.objects.all().delete()
        Customer.objects.all().delete()
        TestCase.tearDown(self)

    def test_transaction_1_stamp_previous_balance_0(self):
        """
        Create a simple transaction that earns 1 stamp
        """
        transaction = Transaction.objects.create(customer=self.customer)
        TransactionLine.objects.create(transaction=transaction, product=self.widget, quantity=1)
        self.assertEqual(1, self.customer.balance)
        self.assertEqual(0, Voucher.objects.filter(customer=self.customer).count())

    def test_transaction_10_stamps_previous_balance_0(self):
        """
        Create a simple transaction that earns a voucher
        """
        before = Voucher.objects.filter(customer=self.customer).count()
        transaction = Transaction.objects.create(customer=self.customer)
        TransactionLine.objects.create(transaction=transaction, product=self.widget, quantity=10)
        self.assertEqual(10, Stamp.objects.filter(transaction_line__transaction__customer=self.customer, voucher__isnull=False).count())
        self.assertEqual(0, self.customer.balance)
        self.assertEqual(1, Voucher.objects.filter(customer=self.customer).count()-before)


class TestStamps(TestCase):

    fixtures = ['transactions.json']

    def test_show_how_many_stamps_a_customer_has(self):
        c1 = Customer.objects.get(pk=1)
        self.assertEqual(2, c1.balance)

    def test_add_stamps_to_a_customer(self):
        c2 = Customer.objects.get(pk=2)
        before = c2.balance
        Stamp.objects.create(customer=c2)
        self.assertEqual(1, c2.balance-before)

    def test_add_10_stamps_creates_voucher(self):
        """
        Give a customer 10 stamps creates a voucher
        """
        c1 = Customer.objects.get(pk=1)
        before = Voucher.objects.filter(customer=c1).count()
        for x in range(0,10):
            Stamp.objects.create(customer=c1)
        self.assertEqual(1, Voucher.objects.filter(customer=c1).count()-before)


class TestVouchers(TestCase):

    fixtures = ['transactions.json']

    def test_show_how_many_vouchers_a_customer_has(self):
        c1 = Customer.objects.get(pk=1)
        self.assertEqual(1, c1.unredeemed_vouchers)

    def test_add_vouchers_to_a_customer(self):
        c1 = Customer.objects.get(pk=1)
        before = c1.unredeemed_vouchers
        Voucher.objects.create(customer=c1)
        self.assertEqual(1, c1.unredeemed_vouchers-before)

    def test_mark_a_voucher_as_redeemed(self):
        c1 = Customer.objects.get(pk=1)
        before = c1.unredeemed_vouchers
        self.assertTrue(c1.redeem_voucher())
        self.assertEqual(1, before-c1.unredeemed_vouchers)

    def test_no_voucher_to_redeem(self):
        c2 = Customer.objects.get(pk=2)
        self.assertFalse(c2.redeem_voucher())
