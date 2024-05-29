# core/views.py
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
import subprocess
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'yasha/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'yasha/login.html', {'form': form})

@csrf_exempt
def run_code(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        code = data.get('code', '')
        try:
            result = subprocess.run(['python3', '-c', code], capture_output=True, text=True, timeout=5)
            return JsonResponse({'output': result.stdout or result.stderr})
        except subprocess.TimeoutExpired:
            return JsonResponse({'output': 'Code execution timed out'})
    return JsonResponse({'output': 'Invalid request'})

def editor(request):
    return render(request, 'yasha/editor.html')
