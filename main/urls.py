from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('error', views.handler_error, name='error'),
]