from django.template.response import TemplateResponse
from django.shortcuts import render
from django.http import HttpResponse
from .forms import RegistrationForm
from django import forms
from .models import Buyer, Game



def index(request):
    pagename = 'Главная'
    context = {
        'pagename': pagename
    }
    return render(request, 'index.html', context)

def store(request):
    pagename = 'Магазин'
    games = Game.objects.all()
    context = {
        'pagename': pagename,
        'games': games
    }
    return render(request, 'store.html', context)

def basket(request):
    pagename = 'Корзина'
    context = {
        'pagename': pagename
    }
    return render(request, 'basket.html', context)



info = {}
def condition(name, password, repeat_pass, age):
    user_list = Buyer.objects.all()
    for user in user_list:
        if user.name == name:
            info['error'] = 'Пользователь уже существует'
            return info
    if password != repeat_pass:
        info['error'] = 'Пароли не совпадают'
        return info
    if age < 18:
        info['error'] = 'Вы должны быть старше 18'
        return info
    else:
        info['name'] = name
        info['password'] = password
        info['age'] = age
        buyer = Buyer(name=name, age=age)
        buyer.save()
        return info


def sign_up_by_django(request):
    info = {'form': RegistrationForm()}
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            password = form.cleaned_data.get('password')
            repeat_pass = form.cleaned_data.get('repeat_pass')
            age = form.cleaned_data.get('age')
            info_1 = condition(name, password, repeat_pass, age)
            context = info|info_1

        return render(request, 'registration_page_django.html', context=context)

    return render(request, 'registration_page_django.html', context=info)

