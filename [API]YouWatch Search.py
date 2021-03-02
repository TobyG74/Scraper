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
url = bsoup("https://youwatch.site/?s=vagabond&post_type%5B%5D=post&post_type%5B%5D=tv")
for tobz in url.findAll('article', class_='col-md-20 item has-post-thumbnail'):
    title = tobz.h2.text.replace('\nNonton Drama Korea ','').replace('\nNonton ','').replace('\nDownload Drama Korea ','')
    link = tobz.a['href']
    image = tobz.img['src']
    type = tobz.find('div', class_='gmr-posttype-item').text
    txt = bsoup(link)
    info = txt.findAll('div', class_='gmr-movie-innermeta')
    genre = info[0].find('span', class_='gmr-movie-genre').text.replace('Genre: ','')
    year = info[1].find('span', class_='gmr-movie-genre').text.replace('Tahun: ','')
    views = info[1].find('span', class_='gmr-movie-view').text.replace('Dilihat: ','')
    country = txt.findAll('div', class_='gmr-moviedata')[0].text.replace('Negara:','')
    hasil = hasilnya.append({"title":title,"image":image,"link":link,"type":type,"genre":genre,"year":year,"views":views,"country":country})
print(json.dumps(result,indent=4,ensure_ascii=False))
