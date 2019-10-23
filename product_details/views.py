from django.shortcuts import render
from django.http import HttpResponse as hre
from django.template import Context, Template 
from scraper.productScrape import prdctScrapEr
from scraper.scraperCmp import cmPscraper

def products(request):
    context = {}

    if request.GET:
        link = request.GET['link']
        site = request.GET['site']
        title = request.GET['title']
        context['prdCMp'] = []
        if site == 'bestbuy':
            context['prdtl'] = prdctScrapEr.bestBuyPrdDtl(link)
            fruit = [cmPscraper.amaZonCmp(title),
                    cmPscraper.ebayCmp(title),
                    cmPscraper.newEggCmp(title),
                    cmPscraper.walMartCmp(title),
                    cmPscraper.jetCmp(title),
                    ]
            for i in fruit:
                context['prdCMp'].append(i)            
        if site == 'ebay':
            context['prdtl'] = prdctScrapEr.ebayPrdDtl(link)
            fruit = [cmPscraper.amaZonCmp(title),
                    cmPscraper.bestBuyCmp(title),
                    cmPscraper.newEggCmp(title),
                    cmPscraper.walMartCmp(title),
                    cmPscraper.jetCmp(title),
                    ]
            for i in fruit:
                context['prdCMp'].append(i)
        if site == 'amazon':
            context['prdtl'] = prdctScrapEr.amazonPrdDtl(link, title)
            fruit = [cmPscraper.bestBuyCmp(title),
                    cmPscraper.ebayCmp(title),
                    cmPscraper.newEggCmp(title),
                    cmPscraper.walMartCmp(title),
                    cmPscraper.jetCmp(title),
                    ]
            for i in fruit:
                context['prdCMp'].append(i)
        if site == 'newegg':
            price = request.GET['price']        
            context['prdtl'] = prdctScrapEr.neweggPrdDtl(link, price)
            fruit = [cmPscraper.amaZonCmp(title),
                    cmPscraper.ebayCmp(title),
                    cmPscraper.bestBuyCmp(title),
                    cmPscraper.walMartCmp(title),
                    cmPscraper.jetCmp(title),
                    ]
            for i in fruit:
                context['prdCMp'].append(i) 
        if site == 'walmart':
            context['prdtl'] = prdctScrapEr.walmartPrdDtl(link)
            fruit = [cmPscraper.amaZonCmp(title),
                    cmPscraper.ebayCmp(title),
                    cmPscraper.newEggCmp(title),
                    cmPscraper.bestBuyCmp(title),
                    cmPscraper.jetCmp(title),
                    ]
            for i in fruit:
                context['prdCMp'].append(i)  
        if site == 'jet':
            context['prdtl'] = prdctScrapEr.jetPrdDtl(link)
            fruit = [cmPscraper.amaZonCmp(title),
                    cmPscraper.ebayCmp(title),
                    cmPscraper.newEggCmp(title),
                    cmPscraper.walMartCmp(title),
                    cmPscraper.bestBuyCmp(title),
                    ]
            for i in fruit:
                context['prdCMp'].append(i)                                   

    return render(request, 'pages/products.html', context)