from bs4 import BeautifulSoup
import requests,json


hasilnya = []
result = {"creator":"Tobz","result": hasilnya}
url = requests.get("https://anoboy.tube")
rtb = BeautifulSoup(url.content,'html5lib')
for rafz in rtb.findAll('div', class_='column-content'):
	link = rtb.a.href
for rafly in rtb.findAll('div', class_='amv'):
	title = "{}".format(str(rafly.find('h3', {'class':'ibox1'}).text))
	image = "{}".format(str(rafly.find('amp-img')['src']))
	date = "{}".format(str(rafly.find('div',class_='jamup').text))
	hasil = hasilnya.append({"link":link,"title":title,"image":image,"date":date})
print(json.dumps(result,indent=4,ensure_ascii=False))