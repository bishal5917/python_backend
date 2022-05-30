from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product

# Create your views here.
def sayHello(request):
    #pk=primary key (django will automatically know it as primary key)
    product=Product.objects.get()
    return render(request,'first.html')
