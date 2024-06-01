from atexit import register
from django.urls import path
from accounts.views import *


urlpatterns = [
    path('', index, name='index'),
    path('register/', register, name='register'),  # Registration view
    path('login/', login, name='login'),  # Login view
    path('logout/', logout, name='logout')
]
