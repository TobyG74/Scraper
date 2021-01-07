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
url = bsoup("https://otakudesu.tv/?s=danmachi&post_type=anime")
for rafly in url.findAll('div', class_='page'):
	image = "{}".format(str(rafly.find('img')['src']))
	link = "{}".format(str(rafly.find('a')['href']))
	data = bsoup(link)
	info = data.find('div', class_='infozingle')
	rafli = info.findAll('p')
	title = rafli[0].text.replace("Judul: ","")
	title2 = rafli[1].text.replace("Japanese: ","")
	rating = rafli[2].text.replace("Skor: ","")
	produser = rafli[3].text.replace("Produser: ","")
	tipe = rafli[4].text.replace("Tipe: ","")
	stat = rafli[5].text.replace("Status: ","")
	episode = rafli[6].text.replace("Total Episode: ","")
	durasi = rafli[7].text.replace("Durasi: ","")
	rilis = rafli[8].text.replace("Tanggal Rilis: ","")
	studio = rafli[9].text.replace("Studio: ","")
	genre = rafli[10].text.replace("Genre: ","")
	info2 = data.find('div', class_='sinopc')
	rafli2 = info2.findAll('p')
	sinopsis = rafli2[0].text
	hasil = hasilnya.append({"judul":title,"judul_jepang":title2,"rating":rating,"produser":produser,"tipe":tipe,"status":stat,"total_episode":episode,"durasi":durasi,"tanggal_rilis":rilis,"studio":studio,"genre":genre,"sinopsis":sinopsis,"thumbnail":image,"link":link})
print(json.dumps(result,indent=4,ensure_ascii=False))