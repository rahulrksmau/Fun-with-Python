# from django.http import HttpResponse
from django.shortcuts import render

# import datetime

"""
def home(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
"""


def req_page(request):
    return render(request, 'index.html', {'name': 'raspberry Pi sender'})


def led_glow(request):
    print ("response", request.GET.get('led'))
    return render(request, 'index.html', {'name': 'raspberry Pi sender'})
