from django import forms

from .models import Account, AnalyticRecord

class CreateAccount(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['login', 'password', 'comment']


class StartCollectingInformation(forms.ModelForm):


    class Meta:
        model = AnalyticRecord
        fields = ['account', 'user']
