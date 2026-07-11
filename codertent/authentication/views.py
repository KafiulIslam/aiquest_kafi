from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from .form import UserForm


def welcome(request):
    return HttpResponse("Welcome to CoderTent!")


# register with UserForm
def register(request):
    # on post request
    if request.method == 'POST':
        register_form = UserForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            return render(request, 'register/register_success.html')

        else:
            register_form = UserForm()

    # on get request
    else:
        register_form = UserForm()

    return render(request, 'register/register_form.html', {'register_form': register_form})


# signup with UserCreationForm
def signup(request):
    # on post request
    if request.method == 'POST':
        signup_form = UserCreationForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            return render(request, 'register/register_success.html')

        else:
            signup_form = UserCreationForm(request.POST)

    # on get request
    else:
        signup_form = UserCreationForm()

    return render(request, 'register/register_form.html', {'register_form': signup_form})
