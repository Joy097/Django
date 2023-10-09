from django.shortcuts import render
import mimetypes
from django.http import FileResponse
from django.conf import settings
import os
from django.http.response import HttpResponse



def download_file(request):
    # Define the file path
    file_path = os.path.join(settings.MEDIA_ROOT, 'example.txt')

    # Open the file for reading
    with open(file_path, 'rb') as file:
        response = HttpResponse(file.read(), content_type='application/octet-stream')
        response['Content-Disposition'] = f'attachment; filename="{os.path.basename(file_path)}"'
        return response
    


def say_hello(request): 
    return render(request,'page.html')