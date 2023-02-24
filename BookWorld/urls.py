from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('register/', views.registerUser, name='register'),
    path('cart/', views.cartView, name='cart'),
    path('products/', views.products, name='products'),
    path('products/<int:product_isbn>', views.product, name='product'),
    path('add/<int:product_isbn>', views.add_to_cart, name='add'),
    path('remove/<int:product_isbn>', views.remove_from_cart, name='remove'),
    path('substract/<int:product_isbn>', views.subtract_from_cart, name='subtract'),
    path('clear/<int:product_isbn>', views.clear_cart, name='clear'),

]
