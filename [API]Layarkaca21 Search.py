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
url = bsoup("http://167.99.71.200/?s=cars&post_type%5B%5D=post&post_type%5B%5D=tv")
for tobz in url.findAll('article', attrs={'itemscope':'itemscope'}):
	title = tobz.a['title']
	link = tobz.a['href']
	img = tobz.img['src']
	image = shorturl(img)
	rating = tobz.find('div', class_='gmr-rating-item').text.replace('Rating: ','')+'/10'
	genre_negara = tobz.find('div', class_='gmr-movie-on').text
	hasil = data.append({"judul":title,"thumb":image,"link":link,"rating":rating,"genre_negara":genre_negara})
print(json.dumps(result,indent=4,ensure_ascii=False))