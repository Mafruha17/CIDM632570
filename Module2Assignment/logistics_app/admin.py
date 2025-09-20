from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'order_date', 'client_type', 'delivery_location')
    ##search_fields = ('order_id', 'client_type')