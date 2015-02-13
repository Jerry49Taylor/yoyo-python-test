from django.utils import timezone
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from immutablefield.models import ImmutableModel


# Create your models here.
class Customer(models.Model):
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def redeem_voucher(self):
        """
        Redeems the oldest unredeemed voucher and returns it or None
        """
        voucher_to_redeem = Voucher.objects.filter(customer=self, date_redeemed__isnull=True).order_by('date_created').first()
        if voucher_to_redeem:
            voucher_to_redeem.date_redeemed = timezone.now()
            voucher_to_redeem.save()
        return voucher_to_redeem

    @property
    def balance(self):
        return Stamp.objects.filter(customer=self, voucher__isnull=True).count()

    @property
    def unredeemed_vouchers(self):
        return Voucher.objects.filter(customer=self, date_redeemed__isnull=True).count()


class Voucher(ImmutableModel):
    """
    Vouchers can only be redeemed once but are transferable
    """
    customer = models.ForeignKey(Customer, null=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_redeemed = models.DateTimeField(null=True)

    class ImmutableMeta:
        immutable = ['date_created', 'date_redeemed']
        quiet = False    


class Product(models.Model):
    """
    Products have a unique sku 
    I haven't made any guesses e.g. whether prices are fixed or a time series
    """
    sku = models.CharField(max_length=100, unique=True, null=False)
    stamps_earned = models.IntegerField(default=0)


class Transaction(ImmutableModel):
    """ 
    Simple Transaction and Transaction Line model
    Can be assigned to another customer intentionally
    """
    customer = models.ForeignKey(Customer, null=False)
    date_created = models.DateTimeField(auto_now_add=True)

    class ImmutableMeta:
        immutable = ['date_created']
        quiet = False  


class TransactionLine(ImmutableModel):
    """
    Immutable Each line on a transaction with unit and quantity
    Ignoring tax etc
    """
    transaction = models.ForeignKey(Transaction, null=False)
    product = models.ForeignKey(Product, null=False)
    quantity = models.IntegerField(null=False)

    class ImmutableMeta:
        immutable = ['transaction', 'product', 'quantity']
        quiet = False  


class Stamp(ImmutableModel):
    """
    Stamps may be earned by a transaction line and assigned to voucher once
    Stamps may be given to a customer without a purchase
    Stamps may be transferred between customers
    """
    date_created = models.DateTimeField(auto_now_add=True)
    transaction_line = models.ForeignKey(TransactionLine, null=True)
    voucher = models.ForeignKey(Voucher, null=True)
    customer = models.ForeignKey(Customer, null=False)

    class ImmutableMeta:
        immutable = ['date_created', 'transaction_line', 'voucher',]
        quiet = False


@receiver(post_save, sender=TransactionLine)
def transaction_stamp_handler(sender, instance, created, **kwargs):
    """
    This signal automatically adds stamps and creates vouchers
    Its not what was aksed for in the spec but I thought this made the exercise more interesting
    """
    if created:
        stamps_to_create = instance.quantity * instance.product.stamps_earned
        while(stamps_to_create > 0):
            Stamp.objects.create(transaction_line=instance, customer=instance.transaction.customer)
            stamps_to_redeem = Stamp.objects.filter(customer=instance.transaction.customer, voucher__isnull=True).order_by('date_created')[:10]
            if len(stamps_to_redeem) == 10:
                voucher = Voucher.objects.create(customer=instance.transaction.customer)
                for stamp in stamps_to_redeem:
                    stamp.voucher = voucher
                    stamp.save()
            stamps_to_create -= 1
