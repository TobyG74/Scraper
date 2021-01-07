from bs4 import BeautifulSoup
import requests,json
from requests import get

def bsoup(link,hdr=True):
    CustomHeader = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0"}
    if hdr == False:return BeautifulSoup(requests.get(link).content, "html.parser")
    else:return BeautifulSoup(requests.get(link,headers=CustomHeader).content, "html.parser")
def shorturl(link):return get("https://tinyurl.com/api-create.php?url="+link).text

query = 'jakarta'

data = []
result = {"creator":"Tobz","result": data}
url = bsoup("https://time.is/id/{}".format(query))
for Tobz in url.findAll('div', attrs={'id':'time_section'}):
    title = Tobz.h1.text
    time = Tobz.find('div', attrs={'id':'clock0_bg'}).text
    date = Tobz.find('div', class_='w90 tr clockdate').text
    sun = Tobz.find('span', class_='nw').text
    hasil = data.append({"title":title,"time":time,"date":date,"sun":sun})
print(json.dumps(result,indent=4,ensure_ascii=False))