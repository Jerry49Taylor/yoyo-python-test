from django.contrib import admin

from shop.models import Customer, Product, Stamp, Voucher


# Register your models here.
class StampInline(admin.TabularInline):
    model = Stamp
    extra = 1


class VoucherInline(admin.TabularInline):
    model = Voucher
    extra = 1


class CustomerAdmin(admin.ModelAdmin):
    inlines = [StampInline, VoucherInline]
    list_display = ('first_name', 'last_name', 'balance', 'unredeemed_vouchers')
    list_filter = ['last_name', 'first_name']
    search_fields = ['last_name', 'first_name']


class ProductAdmin(admin.ModelAdmin):
    list_display = ('sku', 'stamps_earned')
    search_fields = ['sku',]

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, ProductAdmin)
