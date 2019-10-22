from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, Template
import http.cookiejar as hcj
import urllib.request as ure
import urllib.parse as upre
import bs4
import requests as re 

def groups(request):
    if request.GET:
        query = request.GET['query']
        key = query.replace('+', '%20')
        
        cj = hcj.CookieJar()

        opener = ure.build_opener(ure.HTTPCookieProcessor(cj))
        
        ure.install_opener(opener)
        
        authentication_url = "https://mbasic.facebook.com/login.php"
        payload = {
        
            'email':"ffries6@gmail.com",
            'pass':"Sa209212"
        }
        data = upre.urlencode(payload).encode('utf-8')
        req = ure.Request(authentication_url, data)
        resp = ure.urlopen(req)
        contents = resp.read()
        
        if contents == '':
            pass
        
        url = "https://mbasic.facebook.com/search/groups/?q="+key+"&source=filter&isTrending=0&cursor=AbqEfEgN5oVu4yMchrwJof8di5SQINc6kS7607_wFYY5KbrXFneWVw4FA4xT1paXP77tRQ_Gdh0myaon00l3R3eqb3sS0-sbe4tRFNeixsdCXoqPwwbj2XpNkh4l3EJW4GUXUVvjDO792IPbgF9rZPS9ihPpjdwDjP94CQiLKFO-zKthBWQKAGMl0mDu_MyEmUVfdox_8pH564juhPhVYq1wfASh-8l7IVTyc6J_dYzeV_6woXcZVL1dk3b3C9tQS6y8cnWwZO3trgydB2zknmxPjOIqPPYzectH5ELgfhqEEkEiq8ftkbenh3HGZEsKwabY00nO0XWZnyD9weHkmswpk5igT_fm4aFXsb5h3eAlXk13oYMsRnynng4cyTaLoK8-8B1Qzh8U7QISfM4p7M2O3ufKFWefI-7Oul-Ku6gjYgNXyzmtCBgvoudn672Nz6Pqei_gxpQZoMoxIPGGy_fSzFmBBs_apTqS3e1791-1p-u6LHuNy850asvCCSkJrv85HYhiFcXyeLbdbyRQhBM2EhsV3NzKWeiqUI8AwizpLzXYaxLOET9a2tpa12sCKXiTI00RYDHd8lxQFT6r0fzvDGghJ-DbGeysyV2oyHlVlM_-tTQTvadWZBqaPCJiAecjhvOOKdU4gzKJ4zB3iRW6xbV_ZzPcyu-D0XIq3sI1s85hbXAQe7fbFOdnurP6JH8SkkWcgRyg1Bp7fj7-BDS4oPEMYlqw6fALwkQmtJX2l6sUHN2wtUuX1M-3Ej3LW4ZgB7BbnBqSjMp0TFJzxQSbmOo3n9U63B_3lYgF4zqs35PsNw-ILuDxqQT5LywyJnddacwgBGsIjC5Crbl6DVAL_AgKxPIdhyxXvfRdabWNeuffzQ0WOUxKSCu1d1bq5AlbQau_fs1-Vs4RU_WO0AtYvpKbwQNxj1lePvj-w-wDcW7vF-I2a_uc2HdqFGxabvrvds4cZC7aAziJmrpoTK5_DyVslUuZOWnSi1dtyRuVnV2R0K05egAHFOGXaYTN3ZTsPdJHQCIAmeJpYjMIQEzokDCOdyetPAgeE52kfmEexPMm6PoSj6OM5Ft88RCJLfQjNd_vkIx76hccnLQR4PFpdEckHgk1Q5W2sZyOFaiZu1xgw1WPjWERyi4mjYRcK1oRvjq4w9Z-hi6f7GjkpyNgara99eyhZZWFjoK4sEDAX8vvTn4DhmU8qS1bvw3fl09fzPoWTdtTaABLo-gj-MaDn9fFVF85kvKW0Iyep8x0fji77RmF28pAh6DaLG6VNXdubWpSPb9hAw-joCK5bi911MGE4cEIothu_QtGJ0oXxFrJ8jeDjCKfvmg_jHxE1gmrR0kUpMtKAvrYed2xOHEMGZOzvGaY-Zz4W2VaGcAttLcDA5nVp4_mRHpMr7pmx8cZjpUxf8CQcxeczdmJTYV1DTXCWdDPJzxcE5G3YNneRUgvonROmHzu1dtIv8P_QBNlxZ_jtdpsGJsO8Kw2sJRepef7Vpe3lD5F4hZs7BSFgzrvqRor8HgwBJDh46Rkclo8UqrUXyH6-jevlu8qg864th4Fao0hPa2Ddhp6wzxG4M7h7iiUTGQ0QKBCsiweWdcIFxy7wX9YNM2OKDlXU54c7RLFiwcxLwxYl3OL9arCb1_BhFTvGVKrqDQf09ibBtbVXmbtfJtqgH_sDoLIgrUeVEdby19A8G5_jAbPkxX802vXWyJlCLz0ygGF8Tud_IFN6eNV4hvLyQCNpxZZWQllnDGmQlijL7FIHIh2MlZeYsAzwcLbgbcnabz1uwtWqgEW0o8eNNO_DDuz1RZX-kRa6FDG2_HyHgm7Ef8H4ApCYG3wM73Q3qBjt-N9FiR_BXBwgFa5KrT5ENpP1RpIddue8C4a6r5Z0B8Nw2GJ5dIcRaynIbFMkq-jf30GCvPCotG9NIPbP2GOk4F3j0TpqXitRVzYfMbkMZuoPMtMSgIrKuVGIzcy81fAH_w9pofXxTriatJsUU2UV4KgQkVMNV1FnrsV2BRDCGr8GmhwCpeU-dfEtpZJ2C6eYbKbH3fZnB4zr9h-5YnM7PnIoxWZQ7U_28szMcINC84O5ROQvpXF4UlYh4Lkn1iE5IJ1sw3zbA3JB-XM6Z9Kfj9b0Ew8zi97&pn=2&usid=c4cd9cf724543f096982b40de733c4b8&tsid&refid=46" #search url
        
        data = re.get(url, cookies=cj) #geting the page data from the search result
        soup = bs4.BeautifulSoup(data.text, 'html5lib') 
        
        items = soup.find("div", {"id":"BrowseResultsContainer"})
        
        allGroup = []
        for item in items.find_all("div", {"class":"bx"}):
            header = item.find("td", {"class":"t ce"})
            title = header.find("a")
            
            link = title['href']
            link2 = link.split('/')[2]
            group_id = link2.split('?')[0]
            
            group_details = title.text.split('Group')
            group_name = group_details[0]
            group_info = group_details[1]
            
            w = '';
            w += '<div class="row shadow-sm mt-4"><div class="col ml-3">';
            w += '<a href="user_view.html?id='+group_id+'" class="btn btn-link w-100"><h5 class="text-primary float-left">'+group_name+'</h5></a>';
            w += '<span class="text-secondary ml-3">'+group_info+'</span>';
            w += '</div></div>';
            
            allGroup.append(w)
        return HttpResponse(allGroup)