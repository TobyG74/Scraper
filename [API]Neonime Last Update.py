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
url = bsoup("https://neonime.vip")
desc = url.find('span', {'class': 'ttx'}).text
for Tobz in url.findAll('div',class_='item episode-home'):
    link = "{}".format(str(Tobz.find('a')['href']))
    title = "{}".format(str(Tobz.find('img')['alt']))
    image = "{}".format(str(Tobz.find('img')['data-src'])).replace(' ',"")
    hasil = data.append({"title":title,"desc": desc,"image":image,"link":link})
print(json.dumps(result,indent=4,ensure_ascii=False))