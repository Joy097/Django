from django.urls import path
from .views import ProductList, Product

urlpatterns = [
    path('', ProductList.as_view(), name='product-list'),
    path('<int:pk>/', Product.as_view(), name='product-detail'),
]
