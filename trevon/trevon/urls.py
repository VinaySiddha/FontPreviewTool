# coding_platform/urls.py
from django.contrib import admin
from django.urls import include, path
from yasha import views
from accounts.views import *
from yasha.views import (
    compile_view,
    problems_view,
    problem_detail_view,
    create_container_view,
    container_detail_view,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('compile/', compile_view, name='compile'),
    path('problems/', problems_view, name='problems'),
    path('problems/<int:problem_id>/', problem_detail_view, name='problem_detail'),
    path('containers/create/', create_container_view, name='create_container'),
    path('containers/<int:container_id>/', container_detail_view, name='container_detail'),
]


