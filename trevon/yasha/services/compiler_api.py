# services/compiler_api.py

import requests
from django.conf import settings

def compile_code(source_code, language):
    url = settings.COMPILER_API_URL
    headers = {
        'Authorization': f'Bearer {settings.COMPILER_API_KEY}',
        'Content-Type': 'application/json'
    }
    payload = {
        'source_code': source_code,
        'language': language
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()
