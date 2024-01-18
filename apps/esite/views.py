from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django import template
from django.urls import reverse

# Create your views here.

def view_landing(request):
    context = {'segment': 'landing_page'}

    #html_template = loader.get_template('esite/home/others/pages-landingpage.html')
    html_template = loader.get_template('esite/home/index.html')
    return HttpResponse(html_template.render(context, request))