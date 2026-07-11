from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render
from .form import UserForm


def welcome(request):
    return HttpResponse("Welcome to CoderTent!")


# auth with UserForm
def register(request):
    # on post request
    if request.method == 'POST':
        register_form = UserForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            return render(request, 'auth/register_success.html')

        else:
            register_form = UserForm()

    # on get request
    else:
        register_form = UserForm()

    return render(request, 'auth/register_form.html', {'register_form': register_form})


# signup with UserCreationForm
def signup(request):
    # on post request
    if request.method == 'POST':
        signup_form = UserCreationForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            return render(request, 'auth/register_success.html')

        else:
            signup_form = UserCreationForm(request.POST)

    # on get request
    else:
        signup_form = UserCreationForm()

    return render(request, 'auth/register_form.html', {'register_form': signup_form})


# login
def login_view(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(request=request, data=request.POST)
        if login_form.is_valid():
            user_name = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=user_name, password=password)
            if user is not None:
                login(request, user)
                return render(request, 'auth/login_success.html')

    else:
        login_form = AuthenticationForm()

    return render(request, 'auth/login_form.html', {'form': login_form})

