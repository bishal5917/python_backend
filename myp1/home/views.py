from django.shortcuts import render
from django.db.models import Q
from store.models import Customer

# Create your views here.


def sayHello(request):
    # pk=primary key (django will automatically know it as primary key)
    # customer = Customer.objects.filter(pk=1)

    # using the Q object (for id<2 or first_name="Boka")
    # customer = Customer.objects.filter(Q(id__lt=2) | Q(first_name="Boka"))

    # order by
    # customer = Customer.objects.order_by('first_name')

    # limiting results
    # customer = Customer.objects.all()[:2]

    # writing raw queries
    customer = Customer.objects.raw("SELECT * FROM store_customers where id=2")

    return render(request, 'first.html', {'cust': customer})
