import requests
import re 

username = 'natas8'
password = 'DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe'
url = 'http://%s.natas.labs.overthewire.org' % username

payload = {'secret': 'oubWYf2kBq', 'submit': 'submit'}

session = requests.Session()

response = session.post(url, data=payload, auth=(username, password))

print(response.text)