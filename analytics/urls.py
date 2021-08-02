from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='analytics'),
    path('start', views.start, name='analytics/start'),
    path('accounts', views.accounts, name='analytics/accounts'),

    #Ajax запросы
    path('ajax/account/delete', views.ajax_delete_account, name='ajax/account/delete'),
    path('ajax/account/create', views.ajax_create_account, name='ajax/account/delete'),
]