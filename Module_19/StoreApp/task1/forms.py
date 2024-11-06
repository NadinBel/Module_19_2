from django.forms import ModelForm
from django import forms
from .models import Buyer

class BuyerForm(forms.ModelForm):
    class Meta:
        model = Buyer
        fields = ('name', 'age',)
class RegistrationForm(BuyerForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Введите пароль')
    repeat_pass = forms.CharField(widget=forms.PasswordInput, label='Повторите пароль')
    class Meta(BuyerForm.Meta):
        fields = (BuyerForm.Meta.fields[0], 'password', 'repeat_pass', BuyerForm.Meta.fields[1],)
