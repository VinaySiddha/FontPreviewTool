# coding_platform/urls.py
from django.contrib import admin
from django.urls import include, path
from yasha import views
from accounts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('login/', views.login_view, name='login'),
    # path('', views.home, name='home'),
    path('run_code/', views.run_code, name='run_code'),
    path('editor/', views.editor, name='editor'),
]


