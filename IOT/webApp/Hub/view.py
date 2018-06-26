# from django.http import HttpResponse
from django.shortcuts import render
from . import main
# import datetime
# Raspberry Pi imports

from .controller_rpi import board, glow

"""
def home(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
"""
def req_page(request):
    return render(request, 'index.html', {'name': 'raspberry Pi sender'})


def led_glow(request):
    # print ("response", request.GET.get('led'))
    led_status =  list(map(int,request.GET.get('led').split('-')))
    main.main(led_status)
    return render(request, 'index.html', {'name': 'raspberry Pi sender'})
