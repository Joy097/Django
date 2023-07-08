from django.urls import path
from . import views

urlpatterns = [
    path('',views.getData),
    path('add/',views.addData),
    path('rem/<int:pk>',views.remove),
    path('upd/<int:pk>',views.update)
]
