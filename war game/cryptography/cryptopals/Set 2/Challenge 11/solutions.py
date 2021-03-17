from Crypto.Cipher import AES
import random

def generationKey():
	key = b''
	for i in range(16):
		key += bytes(chr(random.randint(64, 126)), 'utf-8')
	return key

def Choose_AES(key):
	choice = random.randint(0,1)
	if(choice == 0):
		return AES.new(key, AES.MODE_ECB), True
	else:
		return AES.new(key, AES.MODE_CBC), False

def appendBytes(plaintext):
	before = random.randint(5,10)
	after = random.randint(5,10)

	new_bytes = b''
	for i in range(before):
		new_bytes += bytes(chr(random.randint(0, 127)), 'utf-8')

	new_bytes += plaintext

	for i in range(after):
		new_bytes += bytes(chr(random.randint(0, 127)), 'utf-8')

	return new_bytes


print(appendBytes(b'Hello World'))
