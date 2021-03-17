import hashlib
import random
from Crypto.Cipher import AES

# with open('words.txt') as f:
# 	words = [w.strip() for w in f.readlines()]

# file = open('test.txt', 'w+')


# for i in range(len(words)):
# 	key = hashlib.md5(words[i].encode()).hexdigest()
# 	file.write(key)
# 	file.write('\n')

with open('test.txt') as f:
    password_hash = [w.strip() for w in f.readlines()]

ciphertext = 'c92b7734070205bdf6c0087a751466ec13ae15e6f1bcdd3f3a535ec0f4bbae66'


def decrypt(ciphertext, password_hash):
    ciphertext = bytes.fromhex(ciphertext)
    key = bytes.fromhex(password_hash)

    cipher = AES.new(key, AES.MODE_ECB)
    try:
        decrypted = cipher.decrypt(ciphertext)
    except ValueError as e:
        return {"error": str(e)}

    return {"plaintext": decrypted.hex()}


for i in range(len(password_hash)):
    plaintext = decrypt(ciphertext, password_hash[i])['plaintext']

    try:
        flag = bytes.fromhex(plaintext).decode('utf-8')
        print(flag)
        break
    except ValueError as e:
        continue
