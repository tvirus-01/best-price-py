import bs4
import requests as re
from django.http import HttpResponse
import io

class cmPscraper:
    def cmpTmplt(title, site, img, price, link):
        w = ''
        w += '<div class="cmp-div"><div class="form-group">'
        w += '<h4 class="text-center">'+site+'</h4>'
        w += '</div><div class="form-group">'
        w += '<img src="'+img+'" class="cmp-img">'
        w += '</div><div class="form-group">'
        w += '<h5>'+title+'</h5>'
        w += '<span>'+price+'</span><br>'
        w += '<a class="btn btn-success mt-2" href="'+link+'" target="blank">Buy</a>'
        w += '</div></div>'

        return w

    def amaZonCmp(title):
        title = title.replace('-', '')
        title = title.replace('Brand:', '')
        title = title.replace('Title:', '')
        ttlsplit = title.split(" ")
        query = ''
        nums = [0,1,2,3]
        if len(ttlsplit) <= 4:
            nums = range(len(ttlsplit))
        for num in nums:
            if ttlsplit[num] != '':
                if num == 5:
                    query += ttlsplit[num]
                else:    
                    query += ttlsplit[num]+'+'
        headers = {"User-agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"}
        url = "https://www.amazon.com/s?k="+query+"&ref=nb_sb_noss"
        data = re.get(url,headers=headers)
        soup = bs4.BeautifulSoup(data.text, 'html.parser')

        items = soup.find("div", {"class":"s-result-list"})

        if items == None:
            imgsrc = 'https://cdn.dribbble.com/users/1554526/screenshots/3399669/no_results_found.png'
            link = '#'
            return cmPscraper.cmpTmplt('No Items Found A', 'Amazon', imgsrc, '$00', link)
            #return items 
        else:
            item = items.find("div", {"class":"s-include-content-margin s-border-bottom"})
            if item == None:
                imgsrc = 'https://cdn.dribbble.com/users/1554526/screenshots/3399669/no_results_found.png'
                link = '#'
                return cmPscraper.cmpTmplt('No Items Found B', 'Amazon', imgsrc, '$00', link)
            else:    
                img = item.find("img", {"class":"s-image"})
                imgsrc = img["src"]
                print("imgsrc: "+imgsrc)
                
                header = item.find("h2", {"class":"a-size-mini a-spacing-none a-color-base s-line-clamp-2"})
                if header == None:
                    title = "Title didn't found"
                else:    
                    title = header.find("a").text
                    link = header.find("a")["href"]
                    link  = 'https://www.amazon.com'+link
                print('title'+title)
                pricediv = item.find("a", {"class":"a-size-base a-link-normal s-no-hover a-text-normal"})
                if pricediv == None:
                    price = '00'
                else:    
                    price = pricediv.text
                    price = price.split('$')
                    price = price[1]
                print('price'+price)

                return cmPscraper.cmpTmplt(title, 'Amazon', imgsrc, price, link)

    def bestBuyCmp(title):
        title = title.replace('-', '')
        title = title.replace('Brand:', '')
        title = title.replace('Title:', '')
        ttlsplit = title.split(" ")
        query = ''
        nums = [0,1,2,3]
        if len(ttlsplit) <= 4:
            nums = range(len(ttlsplit))
        for num in nums:
            if ttlsplit[num] != '':
                if num == 5:
                    query += ttlsplit[num]
                else:    
                    query += ttlsplit[num]+'+'
                    
        headers = {"User-agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"}
        url = "https://www.bestbuy.com/site/searchpage.jsp?intl=nosplash&st="+query
        data = re.get(url,headers=headers)
        soup = bs4.BeautifulSoup(data.text, 'html.parser')
        
        items = soup.find('ol', {"class":"sku-item-list"})
        if items == None:
            imgsrc = 'https://cdn.dribbble.com/users/1554526/screenshots/3399669/no_results_found.png'
            link = '#'
            return cmPscraper.cmpTmplt('No Items Found', 'BestBuy', imgsrc, '$00', link)
        else:
            item = items.find("li", {"class":"sku-item"})
            if item == None:    
                imgsrc = 'https://cdn.dribbble.com/users/1554526/screenshots/3399669/no_results_found.png'
                link = '#'
                return cmPscraper.cmpTmplt('No Items Found', 'BestBuy', imgsrc, '$00', link)
            else:
                imgdiv = item.find("div", {"class":"image-column"})
                imgsrc = imgdiv.find('img')['src']

                header = item.find("h4", {"class":"sku-header"})
                title = header.text
                link = "https://bestbuy.com"+header.find("a", href=True)['href']

                pricediv = item.find("div", {"class":"priceView-customer-price"})
                if pricediv == None:
                    price = '$--.00'
                else:    
                    price = pricediv.find("span").text
                return cmPscraper.cmpTmplt(title, 'BestBuy', imgsrc, price, link)   

    def newEggCmp(title):
        title = title.replace('-', '')
        title = title.replace('Brand:', '')
        title = title.replace('Title:', '')
        ttlsplit = title.split(" ")
        query = ''
        nums = [0,1,2,3]
        if len(ttlsplit) <= 4:
            nums = range(len(ttlsplit))
        for num in nums:
            if ttlsplit[num] != '':
                if num == 5:
                    query += ttlsplit[num]
                else:    
                    query += ttlsplit[num]+'+'

        headers = {"User-agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"}
        url = "https://www.newegg.com/p/pl?d="+query
        data = re.get(url,headers=headers)
        soup = bs4.BeautifulSoup(data.text, 'html.parser')
        
        items = soup.find("div", {"class":"items-view"})

        if items == None:            
            imgsrc = 'https://cdn.dribbble.com/users/1554526/screenshots/3399669/no_results_found.png'
            link = '#'
            return cmPscraper.cmpTmplt('No Items Found A', 'New Egg', imgsrc, '$00', link)
        else:
            item = items.find("div", {"class":"item-container"})
            if item == None:
                imgsrc = 'https://cdn.dribbble.com/users/1554526/screenshots/3399669/no_results_found.png'
                link = '#'
                return cmPscraper.cmpTmplt('No Items Found B', 'New Egg', imgsrc, '$00', link)
            else:
                header = item.find("a", {"class":"item-title"})
                title = header.text
                link = header["href"]
                
                img = item.find("a", {"class":"item-img"})
                imgsrc = img.find("img")["src"]           

                price = item.find("li", {"class":"price-current"})
                if price == None:
                    price = '$--'
                else:
                    price = '$'+price.find("strong").text

                return cmPscraper.cmpTmplt(title, 'Newegg', imgsrc, price, link)            

    def walMartCmp(title):
        title = title.replace('-', '')
        title = title.replace('Brand:', '')
        title = title.replace('Title:', '')
        ttlsplit = title.split(" ")
        query = ''
        nums = [0,1,2,3]
        if len(ttlsplit) <= 4:
            nums = range(len(ttlsplit))
        for num in nums:
            if ttlsplit[num] != '':
                if num == 5:
                    query += ttlsplit[num]
                else:    
                    query += ttlsplit[num]+'+'

        headers = {"User-agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"}
        url = "https://www.walmart.com/search/?cat_id=0&query="+query
        data = re.get(url,headers=headers)
        soup = bs4.BeautifulSoup(data.text, 'html.parser')
        
        items = soup.find("div", {"class":"search-product-result"})
        if items == None:                
            imgsrc = 'https://cdn.dribbble.com/users/1554526/screenshots/3399669/no_results_found.png'
            link = '#'
            return cmPscraper.cmpTmplt('No Items Found', 'Walmart', imgsrc, '$00', link)
        else:
            item = items.find("div", {"class":"search-result-listview-item"})
            if item == None:                
                imgsrc = 'https://cdn.dribbble.com/users/1554526/screenshots/3399669/no_results_found.png'
                link = '#'
                return cmPscraper.cmpTmplt('No Items Found', 'Walmart', imgsrc, '$00', link)
            else:
                 imgdiv = item.find("div", {"class":"list-image-wrapper"})
            img = imgdiv.find("img")
            imgsrc = img['src']

            header = item.find("div", {"class":"search-result-product-title"})
            titlecontainer = header.find("a", {"class":"product-title-link"})
            title = titlecontainer.text
            link = "https://www.walmart.com"+titlecontainer["href"]
            
            allprice = item.find("span", {"class":"search-result-productprice"})
            price = allprice.find("span", {"class":"price-group"}).text

            return cmPscraper.cmpTmplt(title, 'Walmart', imgsrc, price, link)        

    def ebayCmp(title):
        title = title.replace('-', '')
        title = title.replace('Brand:', '')
        title = title.replace('Title:', '')
        ttlsplit = title.split(" ")
        query = ''
        nums = [0,1,2,3]
        if len(ttlsplit) <= 4:
            nums = range(len(ttlsplit))
        for num in nums:
            if ttlsplit[num] != '':
                if num == 5:
                    query += ttlsplit[num]
                else:    
                    query += ttlsplit[num]+'+'

        headers = {"User-agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"}
        url = "https://www.ebay.com/sch/i.html?_from=R40&_trksid=m570.l1313&_nkw="+query+"&_sacat=0"
        data = re.get(url,headers=headers)
        soup = bs4.BeautifulSoup(data.text, 'html.parser')

        items = soup.find("ul", {"class":"srp-list"})

        if items ==  None:            
            imgsrc = 'https://cdn.dribbble.com/users/1554526/screenshots/3399669/no_results_found.png'
            link = '#'
            return cmPscraper.cmpTmplt('No Items Found', 'Ebay', imgsrc, '$00', link)
        else:
            item = items.find("div", {"class":"s-item__wrapper"})
            if item ==  None:            
                imgsrc = 'https://cdn.dribbble.com/users/1554526/screenshots/3399669/no_results_found.png'
                link = '#'
                return cmPscraper.cmpTmplt('No Items Found', 'Ebay', imgsrc, '$00', link)
            else:
                info = item.find("div", {"class":"s-item__info"})
            
            header = info.find("a", {"class":"s-item__link"})
            title = header.text
            newtitle = title.replace("SPONSORED", "")
            link = header["href"]
            newlink = link.split("&")[0]
            
            price = info.find("span", {"class":"s-item__price"}).text
            #price = Scraper.priceFiltr(price)

            imgsec = item.find("div", {"class":"s-item__image-section"})
            img = imgsec.find("img", {"class":"s-item__image-img"})["src"] 

            return cmPscraper.cmpTmplt(title, 'Ebay', img, price, link)   

    def jetCmp(title):
        title = title.replace('-', '')
        title = title.replace('Brand:', '')
        title = title.replace('Title:', '')
        ttlsplit = title.split(" ")
        query = ''
        nums = [0,1,2,3]
        if len(ttlsplit) <= 4:
            nums = range(len(ttlsplit))
        for num in nums:
            if ttlsplit[num] != '':
                if num == 5:
                    query += ttlsplit[num]
                else:    
                    query += ttlsplit[num]+'+'

        headers = {"User-agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"}
        url = "https://jet.com/search?term="+query
        data = re.get(url,headers=headers)
        soup = bs4.BeautifulSoup(data.text, 'html.parser')
        
        items = soup.find("div", {"class":"eCjsou"})
        if items == None:            
            imgsrc = 'https://cdn.dribbble.com/users/1554526/screenshots/3399669/no_results_found.png'
            link = '#'
            return cmPscraper.cmpTmplt('No Items Found', 'Jet', imgsrc, '$00', link)
        else:
            item = items.find("div", {"class":"fSSCaC"})            
            if item == None:            
                imgsrc = 'https://cdn.dribbble.com/users/1554526/screenshots/3399669/no_results_found.png'
                link = '#'
                return cmPscraper.cmpTmplt('No Items Found', 'Jet', imgsrc, '$00', link)
            else:
                container = item.find("a", {"class":"cBMJRO"})
            title = container["aria-label"]
            link = "https://jet.com"+container["href"]
            
            price_div = item.find("div", {"class":"idcooA"})
            if price_div == None:
                price = '$--'
            else:
                price = price_div.find("span", {"class":"hIuNJJ"}).text

            imgsrc = 'https://cdn.dribbble.com/users/1554526/screenshots/3399669/no_results_found.png'    

            return cmPscraper.cmpTmplt(title, 'Jet', imgsrc, price, link)              