from django.http import HttpResponse
import time
import datetime


# Create your views here.

def hello(request):
    return HttpResponse('<h1>Hello world!</h1> <br/> <a href="https://www.baidu.com">跳转到百度</a>')


def current_time(request):
    return HttpResponse('<h1>Current time is ' + time.strftime('%Y-%m-%d %H:%M:%S') + '</h1>')


def test(request, offset):
    offset = int(offset)
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    return HttpResponse('ok! offset is ' + str(offset) + ' ' + str(dt))
