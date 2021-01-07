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
url = bsoup("https://moddroid.com/mow-zombies.html")
for tobz in url.findAll('main', class_='col-12 col-lg-8 content-area'):
	image = tobz.img['src']
	txt = tobz.findAll('tr')
	app_name = txt[0].text.replace('App Name','').replace('\n','')
	publisher = txt[1].text.replace('Publisher','').replace('\n','')
	genre = txt[2].text.replace('Genre','').replace('\n','')
	size = txt[3].text.replace('Size','').replace('\n','')
	latest_version = txt[4].text.replace('Latest Version','').replace('\n','')
	mod_info = txt[5].text.replace('Mod Info','').replace('\n','')
	ps_link = txt[6].text.replace('Get it On','').replace('\n','')+txt[6].a['href']
	update = txt[7].text.replace('Update','').replace('\n','')
	dl = tobz.find('a', class_='btn btn-secondary btn-block mb-3')['href']
	dl2 = bsoup(dl)
	download = dl2.find('div', class_='collapse').a['href']
	hasil = data.append({"app_name":app_name,"image":image,"publisher":publisher,"genre":genre,"size":size,"latest_version":latest_version,"mod_info":mod_info,"ps_link":ps_link,"update":update,"download":download})
print(json.dumps(result,indent=4,ensure_ascii=False))