from typing import NoReturn
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup
from csv import writer
import time

#url produktu, sprawdzenie liczby stron z opiniami
url = 'https://www.opineo.pl/opinie-666284-samsung-le40c650.html'

nourl = 2
urls=[]

req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

website = urlopen(req).read()
web_soup = soup(urlopen(url),'html.parser')

nopage = web_soup("span","pagi_page")
nopage = (nopage[-1].string)
nopage = int(nopage)

#przejscie po stronach z opiniami 
for i in range(nopage):
    url_page = 'https://www.opineo.pl/opinie-666284-samsung-le40c650-strona-' + str(nourl) + ',data.html#opinie'
    nourl+=1
    urls.append(url_page)
    #print(urls[i])


for i in range(len(urls)):
    req = Request(urls[i] , headers={'User-Agent': 'Mozilla/5.0'})

    webpage = urlopen(req).read()
    page_soup = soup(webpage, "html.parser")

    title = page_soup.find("title")
    product_name = page_soup.find("span","sh_name").string
    product_name = product_name.replace(" - Opinie","")

    print("Pobieram : " + str(i+1) + "/" + str(len(urls)) + " url ")

    uzytkownicy=[]
    users = page_soup.find_all("span", "revz_nick")
    for user in users:
        uzytkownicy.append(user.string)


    daty=[]
    publish_dates = page_soup.find_all("span","revz_date")
    for date in publish_dates:
        daty.append(date.string)

    komentarze=[]
    div_comments = page_soup.select("div.revz_txt > span")
    for comment in div_comments:
        komentarze.append(comment.string)

    oceny=[]
    grades = page_soup.find_all("span","review_badge")
    for grade in grades:
        oceny.append(grade.text)

    zalety=[]
    advantages = page_soup.find_all("div","ph_asset2 ph_pros2")
    for advantage in advantages:
        if advantage != NoReturn:
            zalety.append(advantage.text)
        else:
            zalety.append("")


    wady=[]
    disadventages = page_soup.find_all("div","ph_asset2 ph_cons2")
    for disadventage in disadventages:
        wady.append(disadventage.text)



    with open('log_opineo.csv', 'a', encoding='utf-8', newline='') as f:
        thewriter = writer(f)
        header = ['Produkt','Uzytkownik', 'Komentarz', 'Ocena', 'Data']
        
        # Naglowek dla pierwszego uruchomienia skryptu
        # if(i==0):
        #     thewriter.writerow(header)


        info = [product_name,uzytkownicy,komentarze,daty,oceny]
        for w in range(len(uzytkownicy)):
            thewriter.writerow([product_name,uzytkownicy[w],komentarze[w],oceny[w],daty[w]])

        f.close()

    time.sleep(10)



