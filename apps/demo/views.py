from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def demo(request):
    context = {'segment': 'demo'}

    html_template = loader.get_template('demo/home/index.html')
    return HttpResponse(html_template.render(context, request))