from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.http import FileResponse
from django.shortcuts import get_object_or_404
from django.views import View
import os
# Create your views here.

def say_hello(request): 
    return render(request,'page.html')


class DownloadFileView(View):
    def get(self, request, file_name):
        
        file_directory = 'templates/'
        file_path = os.path.join(file_directory, file_name)

        if os.path.exists(file_path):
            with open(file_path, 'rb') as file:
                response = FileResponse(file)
                response['Content-Disposition'] = f'attachment; filename="{file_name}"'
                return response
        else:
            return HttpResponseNotFound("File not found")
