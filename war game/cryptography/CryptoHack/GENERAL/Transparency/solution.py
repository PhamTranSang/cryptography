from Crypto.PublicKey import RSA
from Crypto.Util.number import long_to_bytes

with open('transparency.pem') as f:
    key = RSA.import_key(f.read())
    n = key.n

print(n)
