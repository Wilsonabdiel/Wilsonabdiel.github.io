# script_executor/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Use views.index instead of index.views
]
