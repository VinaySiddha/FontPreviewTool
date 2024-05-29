# coding_platform/urls.py
from django.contrib import admin
from django.urls import path
from yasha import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    # path('', views.home, name='home'),
    path('run_code/', views.run_code, name='run_code'),
    path('editor/', views.editor, name='editor'),
]
