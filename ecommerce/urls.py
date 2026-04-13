from django.urls import path
from mysite import settings
from .views import CartDetail, ProductList, ProductDetail, AddToCart, Checkout, RemoveFromCart

urlpatterns = [
    path('products/', ProductList.as_view()),
    path('products/<int:pk>/', ProductDetail.as_view()),
    path('cart/add/', AddToCart.as_view()),
    path('cart/remove/', RemoveFromCart.as_view()),
    path('cart/<int:pk>/', CartDetail.as_view()),
    path('checkout/', Checkout.as_view()),
]
