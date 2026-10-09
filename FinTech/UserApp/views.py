from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return HttpResponse("Hello First page of django")