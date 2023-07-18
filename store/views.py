from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddCatForm
from .models import Category
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
import requests
import json


def home(request):
    url = 'http://127.0.0.1:8000/api/cat/'
    records = requests.get(url).json()

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "You Have Been Logged In!")
            return redirect('home')
        else:
            messages.error(request, "There Was An Error Logging In, Please Try Again...")
            return redirect('home')

    return render(request, 'home.html', {'records': records})



def logout_user(request):
	logout(request)
	messages.success(request, "You Have Been Logged Out...")
	return redirect('home')


def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			# Authenticate and login
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "You Have Successfully Registered! Welcome!")
			return redirect('home')
	else:
		form = SignUpForm()
		return render(request, 'register.html', {'form':form})

	return render(request, 'register.html', {'form':form})




def customer_record(request, pk):
	if request.user.is_authenticated:
		customer_record = Category.objects.get(id=pk)
		return render(request, 'record.html', {'customer_record':customer_record})
	else:
		messages.success(request, "You Must Be Logged In To View That Page...")
		return redirect('home')

def delete_record(request, pk):
    if request.user.is_authenticated:
        url = f'http://127.0.0.1:8000/api/crem/{pk}'
        response = requests.delete(url)
        if response.status_code == 204:
            messages.success(request,  "Category Deleted Successfully...")
        else:
            messages.error(request, f"Failed to delete the record.")
        return redirect('home')
    else:
        messages.error(request, "You Must Be Logged In To Do That...")
        return redirect('home')


def add_record(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = AddCatForm(request.POST)
            if form.is_valid():
                url = 'http://127.0.0.1:8000/api/cadd/'
                response = requests.post(url, data=form.cleaned_data)
                if response.status_code == 201:
                    messages.success(request,  "Category added successfully...")
                else:
                    messages.error(request, f"Failed to add the record.")
                return redirect('home')
        else:
            form = AddCatForm()
        return render(request, 'add_record.html', {'form': form})
    else:
        messages.error(request, "You must be logged in...")
        return redirect('home')

def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Category.objects.get(id=pk)
        if request.method == "POST":
            form = AddCatForm(request.POST, instance=current_record)
            if form.is_valid():
                url = f'http://127.0.0.1:8000/api/cupd/{pk}'
                response = requests.put(url, data=form.cleaned_data)
                if response.status_code == 202:
                    messages.success(request,  "Category updated successfully...")
                else:
                    messages.error(request, "Failed to update the record.")
                return redirect('home')
        else:
            form = AddCatForm(instance=current_record)
        return render(request, 'update_record.html', {'form': form})
    else:
        messages.error(request, "You must be logged in...")
        return redirect('home')
    

from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

from django.http import JsonResponse
def cat_json_view(request):
    with open('cat.json') as file:
        data = json.load(file)
    return JsonResponse(data)


