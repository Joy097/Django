
from django.urls import path
from . import views

urlpatterns = [
    path('get/', views.get_user),
    path('get/<int:pk>', views.get_user),
    path('add/', views.create_user),
    path('del/<int:pk>', views.delete_user),
    path('upd/<int:pk>', views.update_user),
]
