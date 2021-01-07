from bs4 import BeautifulSoup
import requests,json
from requests import get

def bsoup(link,hdr=True):
    CustomHeader = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0"}
    if hdr == False:return BeautifulSoup(requests.get(link).content, "html.parser")
    else:return BeautifulSoup(requests.get(link,headers=CustomHeader).content, "html.parser")
def shorturl(link):return get("https://tinyurl.com/api-create.php?url="+link).text

result = {"creator":"Tobz","source":"kiryuu.co","result": {'rilisan_terbaru':[]}}
url = bsoup("https://kiryuu.co")
for tobz in url.findAll('div', class_='utao'):
	title = tobz.h4.text
	link = tobz.a['href']
	img = tobz.img['src']
	image = shorturl(img)
	info = tobz.findAll('li')
	ch = ''
	ch += info[0].find('a').text + ' - ' + info[0].find('span').text
	ch += 'tumbal' + info[1].find('a').text + ' - ' + info[1].find('span').text
	ch += 'tumbal' + info[2].find('a').text + ' - ' + info[2].find('span').text
	resch = ch.split('tumbal')
	hasil = result['result']['rilisan_terbaru'].append({"title":title,"link":link,"image":image,"chapter":resch})
print(json.dumps(result,indent=4,ensure_ascii=False))