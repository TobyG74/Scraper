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
url = bsoup("https://bacakomik.co/?s=dungeon")
tobz = url.find('div', class_='animepost')
link = tobz.a['href']
soup = bsoup(link)
info = soup.find("div",class_="infox")
txt = info.findAll('span')
status = txt[0].text.replace('Status: ','')
format = txt[1].text.replace('Format: ','')
rilis = txt[2].text.replace('Dirilis: ','')
pengarang = txt[3].text.replace('Pengarang: ','')
jenis = txt[4].text.replace('Jenis Komik: ','')
umur = txt[5].text.replace('Umur Pembaca: ','')
cara = txt[6].text.replace('Cara Baca ','')
konsep = txt[7].text.replace('Konsep Cerita: ','')
update = txt[8].text.replace('Update Terakhir: ','')
dilihat = txt[9].text.replace('Dilihat: ','')
genres = soup.find('div', class_='genre-info').text.replace('\n',', ')
rat = tobz.find('div', class_='rating')
rate = rat.findAll('i')
rating = rate[0].text
for imgz in url.findAll('div', class_='animepost'):
	title = imgz.img['title']
	img = imgz.img['src']
	image = shorturl(img)
	hasil = hasilnya.append({"judul":title,"thumbnail":image,"rating":rating,"link":link,"status":status,"format":format,"dirilis":rilis,"pengarang":pengarang,"jenis_komik":jenis,"umur_pembaca":umur,"cara_baca":cara,"konsep_cerita":konsep,"update_terakhir":update,"genre":genres})
print(json.dumps(result,indent=4,ensure_ascii=False))