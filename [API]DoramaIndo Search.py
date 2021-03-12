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
url = bsoup("https://doramaindo.id/?s=love&post_type=series")
for tobz in url.findAll('div', class_='resultnime'):
    title = tobz.a['title']
    link = tobz.a['href']
    image = tobz.img['src']
    status = tobz.findAll('div', class_='genrestrike')[0].a.text
    genre = tobz.findAll('div', class_='genrestrike')[1].a.text
    hasil = hasilnya.append({"title":title,"link":link,"image":image,"status":status,"genre":genre})
print(json.dumps(result,indent=4,ensure_ascii=False))
