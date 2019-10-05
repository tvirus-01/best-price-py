from django.shortcuts import render
from django.http import HttpResponse as hre
from django.template import Context, Template 
from .choices import site_choices, site_logo_choices
from scraper.scrapers import Scraper

def index(request):
    context = {
        'site_choices': site_choices,
        'site_logo_choices' : site_logo_choices
    }
    return render(request, 'pages/index.html', context)

def search(request):
    context = {}
    if request.GET:
        search_query = request.GET['sq']
        site = request.GET['site_selected']
        context['query'] = str(search_query)
        context['site'] = str(site)
        
        if site == 'bestbuy':
            context['bb'] = Scraper.bestBuyList(search_query)
        elif site == 'amazon':
            context['bb'] = Scraper.amazonList(search_query)  
        elif site == 'ebay':
            context['bb'] = Scraper.ebayList(search_query)
        elif site == 'newegg':
            context['bb'] = Scraper.neweggList(search_query)
        elif site == 'walmart':
            context['bb'] = Scraper.walmartList(search_query)
        elif site == 'jet':
            context['bb'] = Scraper.jetList(search_query)      
        
    return render(request, 'pages/search.html', context)
