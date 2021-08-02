from django.shortcuts import render

from django.shortcuts import redirect
from .models import Account


def main(request):
    return render(request, 'analytics/main.html')


def start(request):
    pass


def accounts(request):
    content = {
        'accounts':Account.objects.all(),
    }
    return render(request, 'analytics/accounts.html', content)


#Ajax запросы
def ajax_delete_account(request):
    if not request.POST:
        return redirect('/main/error')


def ajax_create_account(request):
    if not request.POST:
        redirect('/main/error')