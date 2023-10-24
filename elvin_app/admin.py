from django.contrib import admin
from .models import Order, OrderItem, Customer, Category, Product, DeliveryAddress


# Register your models here.



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'img', 'desc', 'price']


@admin.register(DeliveryAddress)
class DeliveryAddressAdmin(admin.ModelAdmin):
    list_display = ['customer', 'order', 'address', 'phone_number']
# Register your models here.


admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Customer)
