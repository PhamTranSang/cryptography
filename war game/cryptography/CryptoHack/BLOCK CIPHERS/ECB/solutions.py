import requests

string_sent = 'a'*16

base_URL = 'http://aes.cryptohack.org/ecb_oracle'

encrypt_URL = '%s/encrypt/%s' % (base_URL, string_sent)

r = requests.get(encrypt_URL)

ciphertext = r.json()['ciphertext']

print(ciphertext)