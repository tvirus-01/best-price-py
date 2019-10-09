import bs4
import requests as re
from django.http import HttpResponse

class Scraper:
    def prdTmplt(imgsrc, title, price, link, site):
        w = ''
        w += '<div class="row mt-5 shadow-sm p-2">'
        w += '<div class="search-img-div">'
        w += '<img src="'+imgsrc+'">'
        w += '</div><div class="search-info-div">'
        w += '<a href="products?link='+link+'&site='+site+'"><h4>'+title+'</h4></a>'
        w += '<span>$'+price+'</span>'
        w += '</div></div>'

        return w

    def priceFiltr(price):
        newprice = price.split('$')
        newprice = newprice[1]
        return newprice

    def bestBuyList(query, site):
        headers = {"User-agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"}
        url = "https://www.bestbuy.com/site/searchpage.jsp?intl=nosplash&st="+query
        data = re.get(url,headers=headers)
        soup = bs4.BeautifulSoup(data.text, 'html.parser')
        items = soup.find('ol', {"class":"sku-item-list"})
        
        prdList = []
        for item in items.find_all("li", {"class":"sku-item"}):
            header = item.find("h4", {"class":"sku-header"})
            title = header.text
            link = "https://bestbuy.com"+header.find("a", href=True)['href']
            
            pricediv = item.find("div", {"class":"priceView-customer-price"})
            price = pricediv.find("span").text
            price = Scraper.priceFiltr(price)

            img = item.find("img", {"class":"product-image"})["src"]
            imgsrc = img.split(';')[0]

            prdList.append(Scraper.prdTmplt(imgsrc, title, price, link, site))
            #return str(Scraper.prdTmplt(imgsrc, title, price, link))

        allProduct = prdList
        return allProduct

    def amazonList(query, site):
        headers = {"User-agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"}
        url = "https://www.amazon.com/s?k="+query+"&ref=nb_sb_noss_1"
        data = re.get(url,headers=headers)
        soup = bs4.BeautifulSoup(data.text, 'html.parser')
        
        items = soup.find("div", {"class":"s-result-list"})
        
        prdList = []
        for item in items.find_all("div", {"class":"sg-col-20-of-24 s-result-item sg-col-0-of-12 sg-col-28-of-32 sg-col-16-of-20 sg-col sg-col-32-of-36 sg-col-12-of-16 sg-col-24-of-28"}):
            img = item.find("img", {"class":"s-image"})
            imgsrc = img["src"]
            
            header = item.find("h2", {"class":"a-size-mini a-spacing-none a-color-base s-line-clamp-2"})
            if header == None:
                title = "Title didn't found"
            else:    
                title = header.find("a").text
                link = header.find("a")["href"]
            
            pricediv = item.find("a", {"class":"a-size-base a-link-normal s-no-hover a-text-normal"})
            if pricediv == None:
                price = '$--'
            else:    
                price = pricediv.text
                price = price.split('$')
                price = price[1]               

            prdList.append(Scraper.prdTmplt(imgsrc, title, price, link, site))
            #return imgsrc+'||'+title+'||'+price+'||'+link

        allProduct = prdList
        return allProduct     
           
    def ebayList(query, site):
        headers = {"User-agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"}
        url = "https://www.ebay.com/sch/i.html?_from=R40&_trksid=m570.l1313&_nkw="+query+"&_sacat=0"
        data = re.get(url,headers=headers)
        soup = bs4.BeautifulSoup(data.text, 'html.parser')

        items = soup.find("ul", {"class":"srp-list"})

        prdList = []
        for item in items.find_all("div", {"class":"s-item__wrapper"}):
            info = item.find("div", {"class":"s-item__info"})
            
            header = info.find("a", {"class":"s-item__link"})
            title = header.text
            newtitle = title.replace("SPONSORED", "")
            link = header["href"]
            newlink = link.split("&")[0]
            
            price = info.find("span", {"class":"s-item__price"}).text
            price = Scraper.priceFiltr(price)

            imgsec = item.find("div", {"class":"s-item__image-section"})
            img = imgsec.find("img", {"class":"s-item__image-img"})["src"]

            prdList.append(Scraper.prdTmplt(img, title, price, newlink, site))
                    
        allProduct = prdList
        return allProduct  
           
    def neweggList(query, site):
        headers = {"User-agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"}
        url = "https://www.newegg.com/p/pl?d="+query
        data = re.get(url,headers=headers)
        soup = bs4.BeautifulSoup(data.text, 'html.parser')
        
        items = soup.find("div", {"class":"items-view"})
        
        prdList = []
        for item in items.find_all("div", {"class":"item-container"}):
            header = item.find("a", {"class":"item-title"})
            title = header.text
            link = header["href"]
            
            img = item.find("a", {"class":"item-img"})
            imgsrc = img.find("img")["src"]           

            price = item.find("li", {"class":"price-current"})
            if price == None:
                price = '$--'
            else:
                price = price.find("strong").text    

            prdList.append(Scraper.prdTmplt(imgsrc, title, price, link, site))

        allProduct = prdList
        return allProduct    

    def walmartList(query, site):
        headers = {"User-agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"}
        url = "https://www.walmart.com/search/?cat_id=0&query="+query
        data = re.get(url,headers=headers)
        soup = bs4.BeautifulSoup(data.text, 'html.parser')
        
        items = soup.find("div", {"class":"search-product-result"})
        
        prdList = []
        for item in items.find_all("div", {"class":"search-result-listview-item"}):
            imgdiv = item.find("div", {"class":"list-image-wrapper"})
            img = imgdiv.find("img")
            imgsrc = img['src']

            header = item.find("div", {"class":"search-result-product-title"})
            titlecontainer = header.find("a", {"class":"product-title-link"})
            title = titlecontainer.text
            link = "https://www.walmart.com"+titlecontainer["href"]
            
            allprice = item.find("span", {"class":"search-result-productprice"})
            price = allprice.find("span", {"class":"price-group"}).text      
            price = Scraper.priceFiltr(price)

            prdList.append(Scraper.prdTmplt(imgsrc, title, price, link, site))  


        allProduct = prdList
        return allProduct     

    def jetList(query, site):
        headers = {"User-agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"}
        url = "https://jet.com/search?term="+query
        data = re.get(url,headers=headers)
        soup = bs4.BeautifulSoup(data.text, 'html.parser')
        
        items = soup.find("div", {"class":"eCjsou"})
        
        prdList = []
        for item in items.find_all("div", {"class":"fSSCaC"}):
            container = item.find("a", {"class":"cBMJRO"})
            title = container["aria-label"]
            link = "https://jet.com"+container["href"]
            
            price_div = item.find("div", {"class":"idcooA"})
            if price_div == None:
                price = '$--'
            else:
                price = price_div.find("span", {"class":"hIuNJJ"}).text
                price = Scraper.priceFiltr(price)    

            prdList.append(Scraper.prdTmplt('https://images.unsplash.com/photo-1568650620424-23336b69ba8b?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=750&q=80', title, price, link, site)) 

        allProduct = prdList
        return allProduct           