from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='analytics'),
    path('start', views.start, name='analytics/start'),
    path('accounts', views.accounts, name='analytics/accounts'),
    path('analysts', views.analysts, name='analysts'),
    path('account/delete/<int:id>', views.delete_account, name='account/delete'),
]