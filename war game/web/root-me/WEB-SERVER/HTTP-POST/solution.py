import requests

url = 'http://challenge01.root-me.org/web-serveur/ch56/'

data = {'score': '1999999', 'generate': 'Give a try!'}

# r = requests.get(url)
r = requests.post(url, data=data)

print(r.text)