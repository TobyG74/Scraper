from bs4 import BeautifulSoup
import requests,json,random
from requests import get
from base64 import b64encode
from json import dumps

def bsoup(link,hdr=True):
    CustomHeader = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0"}
    if hdr == False:return BeautifulSoup(requests.get(link).content, "html.parser")
    else:return BeautifulSoup(requests.get(link,headers=CustomHeader).content, "html.parser")
def shorturl(link):return get("https://tinyurl.com/api-create.php?url="+link).text

data = []
result = {"creator":"Tobz","result": data}
url = bsoup("https://www.happymod.com/search.html?q=coc")
tobz = url.find('div', class_='pdt-app-box')
title = tobz.h3.text
link = "https://www.happymod.com"+tobz.a['href']
image = tobz.img['data-original']
url2 = bsoup(link)
info = url2.find('div', class_='pdt-app-box')
title = info.h1.text
dl = url2.find('div', class_='pdt-download')
dl1 = "https://www.happymod.com"+dl.a['href']
dl2 = bsoup(dl1)
download = "https://www.happymod.com"+dl2.find('div', class_='new-down-title-box').a['href']
dlshort = shorturl(download)
tobz2 = url2.find('div', class_='new-div-box new-pdt-bg-box')
txt = tobz2.findAll('li')
version = txt[0].text.replace('- Version: ','')
size = txt[1].text.replace('- Size: ','')
price = txt[2].text.replace('- Price: ','')
root = txt[3].text.replace('- Root needed: ','')
purchase = txt[4].text.replace('- Offers In-App Purchase: ','')
data.append({"title":title,"link":link,"image":image,"version":version,"size":size,"price":price,"root":root,"purchase":purchase,"download":dlshort})
print(json.dumps(result,indent=4,ensure_ascii=False))