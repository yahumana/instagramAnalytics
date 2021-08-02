from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import redirect

from .models import Account
from .forms import CreateAccount


def main(request):
    return render(request, 'analytics/main.html')


def start(request):
    pass


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
