import datetime
import time

import pymysql
from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.template import Template, Context

from common import read_file_list
from demo.models import Province, City, Area


# Create your views here.
def index(request):
    return render(request, 'index.html')


def hello(request):
    return HttpResponse('<h1>Hello world!</h1> <br/> <a href="https://www.baidu.com">跳转到百度</a>')


def current_time(request):
    return HttpResponse('<h1>Current time is ' + time.strftime('%Y-%m-%d %H:%M:%S') + '</h1>')


def test(request, offset):
    offset = int(offset)
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    return HttpResponse('ok! offset is ' + str(offset) + ' ' + str(dt))


def get_names(request):
    db = pymysql.Connect('localhost', 'django', 'zx123456', 'django', 3306, charset='utf8')
    cursor = db.cursor()
    cursor.execute('select name from django.province')
    names = [row[0] for row in cursor.fetchall()]
    db.close()
    return render_to_response('index.html', {'names': names})


def notice(request):
    raw_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Ordering notice</title>
</head>
<body>
<h1>Ordering notice</h1>
<p>Dear {{ person_name }}</p>
<p>Thanks for placing an order from {{ company }}. It's scheduled to
ship on {{ ship_date|date:"F j, Y" }}.</p>

<p>Here are the items you've ordered:</p>
<table>
{% for item in item_list %}
    {% if forloop.first %}
    <tr><th>ID</th><th>NAME</th></tr>
    <tr><td>{{ forloop.counter }}</td><td>{{ item }}</td></tr>
    {% else %}
    <tr><td>{{ forloop.counter }}</td><td>{{ item }}</td></tr>
    {% endif %}
{% endfor %}
</table>

{% if ordered_warranty %}
    <p>Your warranty information will be included in the packaging.</p>
{% else %}
    <p>You didn't order a warranty, so you're on your own when
    the products inevitably stop working.</p>
{% endif %}

<p>Sincerely,<br />{{ company }}</p>
</body>
</html>"""
    t = Template(raw_template)
    raw_context = {'person_name': 'Jason', 'company': 'zshield', 'ship_date': datetime.date(2018, 2, 12),
                   'item_list': ['Python', 'Java', 'C++', 'PHP', 'MySQL'], 'ordered_warranty': 'True'}
    c = Context(raw_context)
    return HttpResponse(t.render(c))


def display_meta(request):
    dict_meta = request.META.items()
    return render_to_response('meta.html', {'meta_list': dict_meta})


def search_form(request):
    return render_to_response('search.html')


def search_result(request):
    search_str = request.GET['q']
    if search_str == '':
        return render_to_response('search.html', {'message': '请输入正确的查询关键字'})
    else:
        province_list = Province.objects.filter(name__icontains=search_str)
        city_list = City.objects.filter(name__icontains=search_str)
        if province_list.__len__() > 0 and city_list.__len__() == 0:
            lists = City.objects.filter(province_code=province_list[0].code)
            search_str = province_list[0].name
        elif city_list.__len__() > 0:
            lists = Area.objects.filter(city_code=city_list[0].code)
            search_str = city_list[0].name
        else:
            return render_to_response('search.html', {'message': '请输入正确的查询关键字'})
    return render_to_response('search.html', {'lists': lists, 'query': search_str})


def get_case_list(request):
    base_path = 'E:\\working\\wutaishan45\\cases'
    file_list = read_file_list(base_path)
    return render_to_response('case_list.html', {'data': file_list})
