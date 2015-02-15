import json

from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST, require_GET

from models import Customer, Product, Transaction, TransactionLine, Stamp, Voucher


# Create your views here.
def fail(reason):
    return JsonResponse(dict(success=False, reason=reason))

def success(**kwargs):
    return JsonResponse(dict(success=True, **kwargs))

@require_POST
@login_required
def create_transaction(request, customer_id):
    """
    POST /create_transaction/<customer_id>/
    data = JSON "lines": ["product_id":<product_id>, "quantity":<int>, "product_id":<product_id>, "quantity":<int>, ...]}
    Creates a new transaction for the specified customer.
    example JSON {"lines": ["product_id":1, "quantity":2]} returns JSON {"success": "True"}
    """
    data = json.loads(request.body)
    customer = get_object_or_404(Customer, pk=int(customer_id))
    transaction = Transaction.objects.create(customer=customer)
    for line in data.get('lines'):
        product = get_object_or_404(Product, sku=line.get('sku'))
        TransactionLine.objects.create(transaction=transaction, product=product, quantity=line.get('quantity'))
    return success()

@require_GET
@login_required
def get_stamp_count(request, customer_id):
    """
    GET /get_stamp_count/<customer_id>/
    Returns the balance of unused stamps for the customer_id returns JSON {"success": "True", count:"1"}
    """
    customer = get_object_or_404(Customer, pk=int(customer_id))
    return success(count=customer.balance)

@require_GET
@login_required
def get_voucher_count(request, customer_id):
    """
    GET /get_voucher_count/<customer_id>/
    Returns the balance of unredeemed vouchers for the customer_id returns JSON {"success": "True", count:"1"}
    """
    customer = get_object_or_404(Customer, pk=int(customer_id))
    return success(count=customer.unredeemed_vouchers)

@require_POST
@login_required
def add_stamps(request, customer_id, stamps):
    """
    POST /add_stamps/<customer_id>/<int>
    Adds int stamps and returns the balance of unused stamps for the customer_id returns JSON {"success": "True", count:"4"}
    """
    if stamps < 1:
        return fail('Invalid number of stamps to add')
    customer = get_object_or_404(Customer, pk=int(customer_id))
    for x in range (0, stamps):
        Stamp.objects.create(customer=customer)
    return success(count=customer.balance)

@require_POST
@login_required
def add_vouchers(request, customer_id, vouchers):
    """
    POST /add_vouchers/<customer_id>/<int>
    Adds int vouchers and returns the balance of unredeemed vouchers for the customer_id returns JSON {"success": "True", count:"4"}
    """
    customer = get_object_or_404(Customer, pk=int(customer_id))
    for x in range (0, vouchers):
        Voucher.objects.create(customer=customer)
    return success(count=customer.unredeemed_vouchers)

@require_POST
@login_required
def redeem_voucher(request, customer_id):
    """
    POST /redeem_voucher/<customer_id>
    Redeems oldest unredeemed vouchers for the customer_id returns JSON {"success": "True"}
    if customer has at least one unredeemed voucher or JSON {"success": "True", "reason": "No unredeemed vouchers"}
    """
    customer = get_object_or_404(Customer, pk=int(customer_id))
    return success() if customer.redeem_voucher() else fail(reason='No unredeemd vouchers')
