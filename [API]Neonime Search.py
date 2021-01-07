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
url = bsoup("https://neonime.vip")
desc = url.find('span', {'class': 'ttx'}).text
for Tobz in tbz.find_all('div',class_='item episode-home'):
    link = "{}".format(str(Tobz.find('a')['href']))
    title = "{}".format(str(Tobz.find('img')['alt']))
    image = "{}".format(str(Tobz.find('img')['data-src'])).replace(' ',"")
    data = bsoup(link)
    info = data.find('div', class_='ladoA')
    upload = info.findAll('div', class_='meta-a').text
    data2 = info.find('div', class_='meta-b')
    info2 = data2.findAll('span', class_='metx')
    season = info2[0].text.replace(' Season ','')
    episode = info2[1].text.replace(' Episode ','')
    hasil = hasilnya.append({"title":title,"desc": desc,"image":image,"link":link,'diupload':upload,'season':season,'episode':episode})
print(json.dumps(result,indent=4,ensure_ascii=False))