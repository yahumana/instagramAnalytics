from django.shortcuts import render

from analytics.models import Account, AnalyticRecord

# Create your views here.

def main(request):
    content = {
        'accounts':Account.objects.all()[:5],
        'analysts':AnalyticRecord.objects.all()[:5],
    }
    return render(request, 'main/main.html', content)


def handler_error(request, exception=''):
    return render(request, 'error.html')