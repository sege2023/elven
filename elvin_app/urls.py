from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('products/<str:category>/', views.products, name='products'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('increase_count/<int:orderitem_id>/', views.increase_count, name='increase_count'),
    path('decrease_count/<int:orderitem_id>/', views.decrease_count, name='decrease_count')
]
