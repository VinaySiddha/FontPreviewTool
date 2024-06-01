# core/views.py
from django import db
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
import subprocess
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from accounts.firebase_utils import get_firestore_data, set_firestore_data, update_firestore_data, delete_firestore_data 


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

# views.py


def index(request):
    # Example: Read data from Firebase Realtime Database
    ref = db.reference('/')
    data = ref.get()

    return render(request, 'index.html', {'data': data})

