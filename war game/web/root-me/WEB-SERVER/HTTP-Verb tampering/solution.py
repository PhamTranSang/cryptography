import requests

url = 'http://challenge01.root-me.org/web-serveur/ch8/'

r = requests.put(url)

print(r.text)