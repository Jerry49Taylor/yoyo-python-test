
from django.test import TestCase

from models import Customer, Product, Voucher, Stamp, Transaction, TransactionLine


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
        transaction = Transaction.objects.create(customer=self.customer)
        TransactionLine.objects.create(transaction=transaction, product=self.widget, quantity=10)
        self.assertEqual(10, Stamp.objects.filter(transaction_line__transaction__customer=self.customer, voucher__isnull=False).count())
        self.assertEqual(0, self.customer.balance)
        self.assertEqual(1, Voucher.objects.filter(customer=self.customer).count())


class TestStamps(TestCase):

    fixtures = ['transactions.json']

    def test_show_how_many_stamps_a_customer_has(self):
        c1 = Customer.objects.get(pk=1)
        self.assertEqual(2, c1.balance)

    def add_stamps_to_a_customer(self):
        pass


class TestVouchers(TestCase):

    fixtures = ['transactions.json']

    def show_how_many_vouchers_a_customer_has(self):
        c1 = Customer.objects.get(pk=1)
        self.assertEqual(2, c1.unredeemed_vouchers)
        pass

    def add_vouchers_to_a_customer(self):
        pass

    def mark_a_voucher_as_redeemed(self):
        pass
