from django.shortcuts import render
from django.http import HttpResponse as hre
from django.template import Context, Template 
from scraper.productScrape import prdctScrapEr

def products(request):
    context = {}

    if request.GET:
        link = request.GET['link']
        site = request.GET['site']

        if site == 'bestbuy':
            context['prdtl'] = prdctScrapEr.bestBuyPrdDtl(link)
        if site == 'ebay':
            context['prdtl'] = prdctScrapEr.ebayPrdDtl(link)
        if site == 'amazon':
            title = request.get['title']
            price = request.get['price']
            imgsrc = request.get['imgsrc']
            context['prdtl'] = prdctScrapEr.amazonPrdDtl(link, title, price, imgsrc)
        if site == 'newegg':
            context['prdtl'] = prdctScrapEr.neweggPrdDtl(link) 
        if site == 'walmart':
            context['prdtl'] = prdctScrapEr.walmartPrdDtl(link)  
        if site == 'jet':
            context['prdtl'] = prdctScrapEr.jetPrdDtl(link)                                   

    return render(request, 'pages/products.html', context)