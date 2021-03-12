from bs4 import BeautifulSoup
import requests,json
from requests import get

def bsoup(link,hdr=True):
    CustomHeader = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0"}
    if hdr == False:return BeautifulSoup(requests.get(link).content, "html.parser")
    else:return BeautifulSoup(requests.get(link,headers=CustomHeader).content, "html.parser")
def shorturl(link):return get("https://tinyurl.com/api-create.php?url="+link).text

hasilnya = []
result = {"creator":"Tobz","result": hasilnya}
url = bsoup("https://drakorindo.live/?s=love")
for tobz in url.findAll('article'):
    title = tobz.h3.text.replace('\n\n\t\t\t\t\tDrama Korea ','').replace('\n\n\t\t\t\t\tDrama ','').replace('\t\t\t\t\n','')
    link = tobz.a['href']
    image = tobz.img['src']
    upload = tobz.find('span', class_='mh-meta-date updated').text
    sinopsis = tobz.find('div', class_='mh-excerpt').text.replace('\n','')
    hasil = hasilnya.append({"title":title,"link":link,"image":image,"upload":upload,"sinopsis":sinopsis})
print(json.dumps(result,indent=4,ensure_ascii=False))
