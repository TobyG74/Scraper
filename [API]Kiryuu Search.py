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
url = bsoup("https://kiryuu.co/?s=demon")
for Tobz in url.findAll('div',class_='bs'):
    title = "{}".format(str(Tobz.find('a')['title']))
    img = "{}".format(str(Tobz.find('img')['src']))
    image = shorturl(img)
    link = "{}".format(str(Tobz.find('a')['href']))
    format = Tobz.find('div', class_='limit').text.replace('\n','').replace(' ','')
    chapter = Tobz.find('div', class_='adds').text.replace('\n','')
    rating = Tobz.find('div', class_='numscore').text
    info = bsoup(link)
    gen = info.find('span', class_='mgen').text.replace(' ',', ')
    sinopsis = info.find('div', class_='entry-content entry-content-single').text.replace('\n','')
    follow = info.find('div', class_='bmc').text
    txtz = info.find('div', class_='tsinfo bixbox')
    status = txtz.findAll('div')[0].text.replace('\n','').replace('Status ','').replace('\t','')
    type = txtz.findAll('div')[1].text.replace('\n','').replace('Type ','').replace('\t','')
    hasil = data.append({"title":title,"image":image,"link":link,"format":format,"chapter":chapter,"rating":rating,"follow":follow,"status":status,"type":type,"sinopsis":sinopsis,"genre":gen})
print(json.dumps(result,indent=4,ensure_ascii=False))