from bs4 import BeautifulSoup
import requests,json
from requests import get

url = get("https://api-ssl.bitly.com/v3/shorten?access_token=eeed32b267a6f473e0e824aa685527cf1e18a5e6&longUrl={}".format(query)).json()
data = url['data']['url']
print(data)
result = {status:200,creator:'Tobz','result':data}
print(json.dumps(result,indent=4,ensure_ascii=False))