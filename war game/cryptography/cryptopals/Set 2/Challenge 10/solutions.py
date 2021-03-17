from base64 import b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad


def decrypt(ciphertext, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    try:
        decrypted = unpad(cipher.decrypt(ciphertext), AES.block_size)
    except ValueError as e:
        return e
    return decrypted


key = b'YELLOW SUBMARINE'
iv = chr(0).encode() * AES.block_size
with open('10.txt') as f:
    ciphertext = b64decode(f.read())

print(decrypt(ciphertext, key, iv))
