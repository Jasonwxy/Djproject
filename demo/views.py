from django.shortcuts import render
from django.http import HttpResponse
import time


# Create your views here.

def hello(request):
    return HttpResponse('<h1>Hello world!</h1>')


def current_time(request):
    return HttpResponse('<h1>Current time is ' + time.strftime('%Y-%m-%d %H:%M:%S') + '</h1>')
