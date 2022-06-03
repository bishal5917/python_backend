
from audioop import reverse
from urllib.parse import urlencode
from django.contrib.contenttypes.admin import GenericTabularInline
from django.db.models import Count
from django.contrib import admin
from django.http import HttpRequest
from django.utils.html import format_html
from . import models

# Register your models here.


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']
    ordering = ['first_name', 'last_name']
    list_per_page = 5
    search_fields = ['first_name', 'last_name']


@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'products_count']

    def products_count(self, collection):
        url = (reverse('admin:store_product_changelist')+'?' +
               urlencode({
                   'collection_id': str(collection.id)
               }))

        format_html('<a href="{}">{}</a>', url, collection.products_count)
        return collection.products_count

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            products_count=Count('product')
        )


class OrderItemInline(admin.StackedInline):
    autocomplete_fields = ['product']
    model = models.OrderItem
    min_num=1
    max_num=10


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    autocomplete_fields = ["customer"]
    # inlines = [OrderItemInline]
    list_display = ['id', 'placed_at', 'customer']
