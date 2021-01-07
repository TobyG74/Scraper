from bs4 import BeautifulSoup
import requests,json
from requests import get

def bsoup(link,hdr=True):
    CustomHeader = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0"}
    if hdr == False:return BeautifulSoup(requests.get(link).content, "html.parser")
    else:return BeautifulSoup(requests.get(link,headers=CustomHeader).content, "html.parser")
def shorturl(link):return get("https://tinyurl.com/api-create.php?url="+link).text

data = []
result = {"creator":"Tobz","result": data}
url = bsoup("https://moddroid.com/?s=free")
for tobz in url.findAll('div', class_='col-12 col-md-6 mb-4'):
	title = tobz.a['title']
	link = tobz.a['href']
	image = tobz.img['src']
	versi = tobz.find('div', class_='text-truncate text-muted d-flex align-items-center').text.replace('\n',' ')
	hasil = data.append({"title":title,"link":link,"image":image,"versi":versi})
print(json.dumps(result,indent=4,ensure_ascii=False))