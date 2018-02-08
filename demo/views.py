from django.shortcuts import render
from django.http import HttpResponse
import time


# Create your views here.

def hello(request):
    return HttpResponse('<h1>Hello world!</h1> <br/> <a href="https://www.baidu.com">跳转到百度</a>')


def current_time(request):
    return HttpResponse('<h1>Current time is ' + time.strftime('%Y-%m-%d %H:%M:%S') + '</h1>')
