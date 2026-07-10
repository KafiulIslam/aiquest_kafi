from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm


def welcome(request):
    return HttpResponse("Welcome to CoderTent!")


def register(request):
    register_form = UserCreationForm()
    return render(request, 'register/register_form.html', {'register_form': register_form})
