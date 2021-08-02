from django import forms

from .models import Account

class CreateAccount(forms.ModelForm):
    login = forms.CharField(label="Login", max_length=50)
    password = forms.CharField(label="Password", max_length=32)
    comment = forms.CharField(label="Comment", max_length=256, widget=forms.Textarea)

    class Meta:
        model = Account
        fields = ['login', 'password', 'comment']


