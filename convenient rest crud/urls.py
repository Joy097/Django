
from django.urls import path
from . import views

urlpatterns = [
    path('apis/',views.UserList),
    path('api/<int:pk>/', views.User_interact)]
