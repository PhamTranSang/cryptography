import base64
from Crypto.Cipher import AES


def decrypt(ciphertext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    try:
        plaintext = cipher.decrypt(ciphertext)
    except ValueError as e:
        return e
    return plaintext


key = 'YELLOW SUBMARINE'.encode()

with open('7.txt') as f:
	ciphertext = base64.b64decode(f.read())

print(decrypt(ciphertext, key))