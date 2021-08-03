from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import redirect

from .models import Account
from .forms import CreateAccount, StartCollectingInformation
from .collecting_information import collecting

def main(request):
    return render(request, 'analytics/main.html')


def start(request):
    if request.method == 'POST':
        form = StartCollectingInformation(request.POST)
        if form.is_valid():
            form.save()
    
    content = {
        'start_form':StartCollectingInformation(),
    }
    return render(request, 'analytics/start.html', content)


def accounts(request):
    if request.method == 'POST':
        form = CreateAccount(request.POST)
        if form.is_valid():
            form.save()


    content = {
        'accounts':Account.objects.all(),
        'create_account_form':CreateAccount,
    }
    return render(request, 'analytics/accounts.html', content)


def delete_account(request, id):
    try:
        Account.objects.filter(id=id).delete()
    except:
        pass
    return redirect('analytics/accounts')


def analysts(request):
    pass