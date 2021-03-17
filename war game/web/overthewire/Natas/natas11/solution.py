import requests
from urllib.parse import unquote
import base64
import re


username = 'natas11'
password = 'U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK'
url = 'http://%s.natas.labs.overthewire.org/' % username

cookies = {'data': 'ClVLIh4ASCsCBE8lAxMacFMOXTlTWxooFhRXJh4FGnBTVF4sFxFeLFMK'}

session = requests.Session()

r = session.get(url, auth=(username, password), cookies=cookies)

content = r.text
flag = re.findall('The password for natas12 is (.*)<br>', content)[0]

# print(base64.b64decode(unquote(session.cookies['data'])).hex())
print(flag)
