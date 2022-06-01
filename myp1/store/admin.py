from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Collection)
# admin.site.register(models.Customer)

@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']
    ordering = ['first_name', 'last_name']
    list_per_page = 5

@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','placed_at','customer']