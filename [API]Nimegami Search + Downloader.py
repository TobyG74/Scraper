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
url = bsoup("https://nimegami.com/?s=danmachi&post_type=post")
tbz = url.find('div', class_='archive')
for tobz in tbz.findAll('article'):
	info = tobz.find('h2', attrs={'itemprop':'name'})
	title = info.a['title']
	link = info.a['href']
	image = tobz.img['src']
	rating = tobz.find('div', class_='rating-archive').text.replace(' ','')
	status = tobz.find('div', class_='term_tag-a').text.replace(' ','')
	tipe = tobz.find('div', class_='terms_tag').text.replace(' ','')
	dalem = bsoup(link)
	data2 = dalem.find('div', class_='info2').findAll('tr')
	alternatif_title = data2[1].text.replace('Judul Alternatif :','')
	durasi_episode = data2[2].text.replace('Durasi Per Episode :','')
	genre = data2[5].text.replace('Kategori :','')
	season_release = data2[6].text.replace('Musim / Rilis :','')
	series = data2[7].text.replace('Series :','')
	subtitle = data2[8].text.replace('Bahasa :','')
	download_batch = dalem.find('div', class_='batch-dlcuy')
	dl = download_batch.findAll('li')
	_360p = dl[0].a['href']
	_480p = dl[1].a['href']
	_720p = dl[2].a['href']
	data.append({"title":title,"alternatif_title":alternatif_title,"subtitle":subtitle,"duration_episode":durasi_episode,"series":series,"season_release":season_release,"genre":genre,"image":image,"link":link,"rating":rating,"status":status,"type":tipe,"download_batch":{"360p":_360p,"460p":_480p,"720p":_720p}})
print(json.dumps(result,indent=4,ensure_ascii=False))