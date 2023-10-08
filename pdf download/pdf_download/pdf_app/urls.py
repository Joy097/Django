from . import views
from django.urls import path
from .views import DownloadFileView

urlpatterns = [
    path('hello/', views.say_hello),
    path('admin/download/<str:file_name>/', DownloadFileView.as_view(), name='download_file'),
]