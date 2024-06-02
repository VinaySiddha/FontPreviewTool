# some_app/models.py
from django.conf import settings
from accounts.models import *

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
