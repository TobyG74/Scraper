from bs4 import BeautifulSoup
import requests,json
from requests import get

url = requests.get("https://tinyurl.com/api-create.php?url={}".format(query))
data = url.text
print(data)
result = {status:200,creator:'Tobz','result':data}
print(json.dumps(result,indent=4,ensure_ascii=False))