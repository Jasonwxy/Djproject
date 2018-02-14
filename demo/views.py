from django.http import HttpResponse
import time
import datetime
from django.template import Template, Context


# Create your views here.

def hello(request):
    return HttpResponse('<h1>Hello world!</h1> <br/> <a href="https://www.baidu.com">跳转到百度</a>')


def current_time(request):
    return HttpResponse('<h1>Current time is ' + time.strftime('%Y-%m-%d %H:%M:%S') + '</h1>')


def test(request, offset):
    offset = int(offset)
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    return HttpResponse('ok! offset is ' + str(offset) + ' ' + str(dt))


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
