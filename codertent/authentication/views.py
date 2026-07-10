from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from .form import UserForm


def welcome(request):
    return HttpResponse("Welcome to CoderTent!")


def register(request):

    if request.method == 'POST':
        register_form = UserForm(request.POST)
    return render(request, 'register/register_form.html', {'register_form': register_form})
