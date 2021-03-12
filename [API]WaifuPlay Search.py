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
url = bsoup("https://waifuplay.net/?s=shingeki")
for tobz in url.findAll('div', class_='flexbox2-item'):
    title = tobz.find('div', class_='flexbox2-title').findAll('span')[0].text
    studio = tobz.find('div', class_='flexbox2-title').findAll('span')[1].text
    score = tobz.find('div', class_='score').text.replace(' ','')
    genre = tobz.find('div', class_='genres').text
    image = tobz.img['src']
    link = tobz.a['href']
    hasil = hasilnya.append({"title":title,"studio":studio,"score":score,"genre":genre,"image":image,"link":link})
print(json.dumps(result,indent=4,ensure_ascii=False))
