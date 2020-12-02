import requests
import re

username = 'natas6'
password = 'aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1'
url = 'http://%s.natas.labs.overthewire.org' % username

payload = {'secret':'FOEIUWGHFEEUHOFUOIU', 'submit': 'submit'}

session = requests.Session()

response = session.post(url, data=payload, auth=(username, password))

print(response.text)