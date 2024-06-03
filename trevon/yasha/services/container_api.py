# services/container_api.py

import requests
from django.conf import settings

def create_container(image):
    url = settings.CONTAINER_API_URL
    headers = {
        'Authorization': f'Bearer {settings.CONTAINER_API_KEY}',
        'Content-Type': 'application/json'
    }
    payload = {
        'image': image
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

def get_container(container_id):
    url = f"{settings.CONTAINER_API_URL}/{container_id}"
    headers = {
        'Authorization': f'Bearer {settings.CONTAINER_API_KEY}',
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()
