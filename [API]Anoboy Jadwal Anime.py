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
url = bsoup("https://anoboy.tube/2015/05/anime-subtitle-indonesia-ini-adalah-arsip-file-kami/")
tobz = url.find('ul', class_='lcp_catlist')
for info in tobz.findAll('li'):
	title = info.a['title'] + ' -' + info.text.replace(info.a['title'], '')
	link = info.a['href']
	hasil = data.append({"judul":title,"link":link})
print(json.dumps(result,indent=4,ensure_ascii=False))