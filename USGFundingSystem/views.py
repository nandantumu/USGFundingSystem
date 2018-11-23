from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404


def home(request):
    return HttpResponse("Welcome to the USG Funding System")
