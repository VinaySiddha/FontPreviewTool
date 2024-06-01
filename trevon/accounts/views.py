# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm, LoginForm

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

# accounts/views.py

from django.shortcuts import render
from .firebase_utils import get_firestore_data, set_firestore_data, update_firestore_data, delete_firestore_data

def index(request):
    if request.method == 'POST':
        data = request.POST.get('data')
        set_firestore_data('your-collection', 'your-document', {'data': data})
    
    data_from_firestore = get_firestore_data('your-collection', 'your-document')
    return render(request, 'index.html', {'data': data_from_firestore})
