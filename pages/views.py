from django.shortcuts import render
from django.http import HttpResponse as hre

def index(request):
    return render(request, 'pages/index.html')
