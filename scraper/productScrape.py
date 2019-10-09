import io
import bs4
import requests as re
from django.http import HttpResponse

class prdctScrapEr:
    def prdTmplT(title, price, img, data, site, sitelogo, link):
        w = ''
        w += '<div class="col">'
        w += '<h3>'+title+'</h3>'
        w += '<span>'+price+'</span>'
        w += '<h5>'+data+'</h5>'
        w += '<span class="h5">Product Site: </span><a href="'+site+'" target="blank"><img src="static/img/logo/'+sitelogo+'" style="width: 5%;"></a>'
        w += '<br><a target="blank" class="btn btn-success" href="'+link+'">Buy Now</a>'
        w += '</div><div class="col">'
        w += '<img class="prdimg" src="'+img+'">'
        w += '</div>'

        return w

    def bestBuyPrdDtl(link):
        site = 'https://www.bestbuy.com'  
        sitelogo = 'bestbuy.png' 

        headers = {"User-agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"}
        url = link+"&intl=nosplash"
        data = re.get(url,headers=headers)
        soup = bs4.BeautifulSoup(data.text, 'html.parser')
        
        title = soup.find("div", {"class":"sku-title"}).text
        
        pricediv = soup.find("div", {"class":"priceView-customer-price"})
        price = pricediv.find("span").text
        
        carousel = soup.find("ol", {"class":"carousel-indicate"})
        
        data_section = soup.find("div", {"class":"data-section"}).text

        imgsrc = {}
        i = 1
        for liist in carousel.find_all("li", {"class":"thumbnail-wrapper"}):
            img = liist.find("img", src=True)["src"]
            src = img.split(';')[0]
            imgsrc[i] = src
            i = i+1
            
        return prdctScrapEr.prdTmplT(title, price, imgsrc[1], data_section, site, sitelogo, link)

    def ebayPrdDtl(link):
        site = 'https://www.ebay.com'  
        sitelogo = 'ebay.png'

        headers = {"User-agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"}
        url = link
        data = re.get(url,headers=headers)
        soup = bs4.BeautifulSoup(data.text, 'html.parser')
        
        header = soup.find("div", {"class":"vi-swc-lsp"})
        title = header.find("h1", {"id":"itemTitle"}).text
        newtitle = title.replace("Details about   ", "")
        
        pricediv = soup.find("div", {"class":"vi-price"})
        if pricediv == None:
            price = '$--'
        else:    
            price1 = pricediv.find("span", {"class":"notranslate"})
            price = price1["content"]
        
        carousel = soup.find("ul", {"class":"icon"})
        
        #model = soup.find("div", {"class":"itmSelector"}).text
        model = ''

        imgsrc = {}
        i = 1
        for liist in carousel.find_all("li"):
            img = liist.find("img")
            imgsrc1 = img["src"]
            newimgsrc = imgsrc1.replace("64", "500")
            imgsrc[i] = newimgsrc
            i = i+1 

        return prdctScrapEr.prdTmplT(title, price, imgsrc[1], model, site, sitelogo, link)


    def amazonPrdDtl(link, title, price, imgsrc):
        site = 'https://www.amazon.com'
        sitelogo = 'amazon.png'
        # headers = {"User-agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"}
        # url = link
        # data = re.get(url,headers=headers)
        # soup = bs4.BeautifulSoup(data.text, 'html.parser')        
        model = ''
        return prdctScrapEr.prdTmplT(title, price, model, site, sitelogo, link)    

    def neweggPrdDtl(link):
        headers = {"User-agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"}
        url = link
        data = re.get(url,headers=headers)
        soup = bs4.BeautifulSoup(data.text, 'html.parser')
        
        title = soup.find("div", {"class":"wrapper"}).text
        price = soup.find("li", {"class":"price-current"})
        if price == None:
            price = "$--"
        else:
            price = price.text    
        
        model = ''
        site = 'newegg'
        sitelogo = 'newegg.png'

        imgdiv = soup.find("div", {"class":"objImages"})
        img = imgdiv.find("img")["src"]
        
        return prdctScrapEr.prdTmplT(title, price, img, model, site, sitelogo, link)

    def walmartPrdDtl(link):
        headers = {"User-agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"}
        url = link
        data = re.get(url,headers=headers)
        soup = bs4.BeautifulSoup(data.text, 'html.parser')
        
        title = soup.find("h1", {"class":"prod-ProductTitle"}).text
        price = soup.find("span", {"class":"price-group"}).text
        
        model = ''
        site = 'walmart'
        sitelogo = 'walmart.png'

        img = soup.find("img", {"class":"hover-zoom-hero-image"})['src']
        src = img.split('?')[0]                

        return prdctScrapEr.prdTmplT(title, price, img, model, site, sitelogo, link)

    def jetPrdDtl(link):
        headers = {"User-agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"}
        url = link
        data = re.get(url,headers=headers)
        soup = bs4.BeautifulSoup(data.text, 'html.parser')
        
        header = soup.find("div", {"class":"cRczvJ"})
        title = header.find("h1", {"class":"MdBQM"}).text
        
        pricediv = soup.find("div", {"class":"dsOONV"}).text
        
        model = ''
        site = 'jet'
        sitelogo = 'jet.png'

        imgdiv = soup.find("div", {"class":"dMYUrf"})
        img = imgdiv.find("img")['src'] 
        print(img)
        return prdctScrapEr.prdTmplT(title, pricediv, img, model, site, sitelogo, link) 
