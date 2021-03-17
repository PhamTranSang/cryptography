from Crypto.Cipher import AES
import base64


def encrypt(plaintext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    try:
        encrypted = cipher.encrypt(plaintext)
    except ValueError as e:
        return e
    return encrypted


def decrypt(ciphertext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    try:
        decrypted = cipher.decrypt(ciphertext)
    except ValueError as e:
        return e
    return decrypted


key = 'abcdefghijklmnop'.encode()
message = 'AAAAAAAAAAAAAAAABBBBBBBBBBBBBBBB'.encode()

ciphertext = encrypt(message, key).hex()


print(ciphertext[:32])
print(ciphertext[32:])
