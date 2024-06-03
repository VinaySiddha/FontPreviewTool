# services/problem_api.py

import requests
from django.conf import settings

def get_problems():
    url = settings.PROBLEM_API_URL
    headers = {
        'Authorization': f'Bearer {settings.PROBLEM_API_KEY}',
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

def get_problem(problem_id):
    url = f"{settings.PROBLEM_API_URL}/{problem_id}"
    headers = {
        'Authorization': f'Bearer {settings.PROBLEM_API_KEY}',
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()
