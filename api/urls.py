from django.urls import path
from . import views

urlpatterns = [
    
    path('cat/',views.getcatData),
    path('cadd/',views.addcatData),
    path('cget/<int:pk>',views.getonecatData),
    path('crem/<int:pk>',views.removecat),
    path('cupd/<int:pk>',views.updatecat)
]
