from bs4 import BeautifulSoup
import requests,json
from requests import get

link = requests.get("https://api.github.com/users/{}".format(username))
jsonnya = link.text
gitprof = json.loads(jsonnya)
username = gitprof['login']
name = gitprof['name']
follower = gitprof['followers']
following = gitprof['following']
biography = gitprof['bio']
location = gitprof['location']
avatar = gitprof['avatar_url']
company = gitprof['company']
email = gitprof['company']
public_repos = gitprof['public_repos']
public_gists = gitprof['public_gists']
twitter_username = gitprof['twitter_username']
url = gitprof['url']
result = {status:200,creator:'Tobz',result{'username':username,'name':name,'follower':follower,'following':following,'biography':biography,'location':location,'avatar':avatar,'company':company,'email':email,'public_repos':public_repos,'public_gists':public_gists,'twitter_username':twitter_username,'url':url}}
print(json.dumps(result,indent=4,ensure_ascii=False))