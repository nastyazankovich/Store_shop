from django.contrib import admin
from .models import Order, OrderItem


# Register your models here.
class OrderItemInline(admin.TabularInline):
    """Делает табуляр модели OrderProduct для связи с таблицей Order"""
    model = OrderItem
    raw_id_fields = ['product']


@admin.register(Order)
class OrderProductAdmin(admin.ModelAdmin):
    """Регистрация модели Order в админке"""
    list_display = ['id', 'first_name', 'last_name', 'email', 'postal_code', 'address', 'city', 'paid', 'created',
                    'updated']
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]

# Register your models here.
