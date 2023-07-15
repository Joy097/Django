from django.urls import path
from . import views

urlpatterns = [
    path('', views.getproducts),
    path('get/<int:pk>/', views.getproduct),
    path('post/', views.postproducts),
    path('put/<int:pk>/', views.putproducts),
    path('del/<int:pk>/', views.delproducts)
]
