from django.shortcuts import render
from django.http import HttpResponse
import time


# Create your views here.

def hello(request):
    return HttpResponse('Hello world!')


def current_time(request):
    return HttpResponse('Current time is' + time.strftime('%Y-%m-%d %H:%M:%S'))

