from django.shortcuts import render
from django.http import HttpResponse as hre
from django.template import Context, Template 
from .choices import site_choices, site_logo_choices

def index(request):
    context = {
        'site_choices': site_choices,
        'site_logo_choices' : site_logo_choices
    }
    return render(request, 'pages/index.html', context)

def search(request):
    return render(request, 'pages/search.html')