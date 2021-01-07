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
url = bsoup("http://149.56.24.226/?s=frozen")
for tobz in url.findAll('div', class_='search-item'):
	title = tobz.a['title']
	img = tobz.img['src']
	image = shorturl(img)
	link = tobz.a['href']
	info = tobz.findAll('p')
	sutradara = info[1].text.replace('Sutradara: ','')
	bintang = info[2].text.replace('Bintang: ','')
	data = bsoup(link)
	info2 = data.find('div', class_='col-xs-10 content')
	txt = info2.findAll('div')
	kualitas = txt[0].text.replace('Kualitas','')
	negara = txt[1].text.replace('Negara','')
	genre = txt[4].text.replace('Genre','')
	imdb = txt[5].findAll('h3')
	imdb0 = imdb[0].text+'/'
	imdb1 = imdb[1].text+' from '
	imdb2 = imdb[2].text+' users'
	terbit = txt[6].text.replace('Diterbitkan','')
	penerjemah = txt[7].text.replace('Penerjemah','').replace('Oleh','')
	dl = data.find('div', class_='download-movie')
	download = dl.a['href']
	hasilnya.append({"judul":title,"image":image,"link":link,"sutradara":sutradara,"bintang_film":bintang,"kualitas":kualitas,"negara":negara,"genre":genre,"imdb":imdb0+imdb1+imdb2,"diterbitkan":terbit,"penerjemah":penerjemah,"download":download})
print(json.dumps(result,indent=4,ensure_ascii=False))