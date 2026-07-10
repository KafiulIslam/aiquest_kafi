from django.shortcuts import render
from django.http import HttpResponse

def welcome(request):
    return HttpResponse("Welcome to CoderTent!")

def register(request):
    return HttpResponse("Please, create an account first")
