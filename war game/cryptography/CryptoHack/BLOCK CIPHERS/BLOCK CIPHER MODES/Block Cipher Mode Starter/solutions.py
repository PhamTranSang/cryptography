import requests
import json

url = 'http://aes.cryptohack.org/block_cipher_starter/'

url_get_ciphertext = '%s/encrypt_flag/' % url

ciphertext = json.loads(requests.get(url_get_ciphertext).text)["ciphertext"]

url_get_plaintext = '%s/decrypt/%s/' % (url, ciphertext)

plaintext = json.loads(requests.get(url_get_plaintext).text)["plaintext"]

flag = bytes.fromhex(plaintext).decode('utf-8') 

print(flag)