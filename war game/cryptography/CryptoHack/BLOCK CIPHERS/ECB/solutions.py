import requests
import string


def remote_encrypt(string_sent):
    string = string_sent.encode().hex()
    r = requests.get('http://aes.cryptohack.org/ecb_oracle/encrypt/%s' %
                     string).json()['ciphertext']
    return r


# chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-+{}'
flag = ''

for k in range(2):
    b = ''
    for i in range(1, 17):
        string_sent = 'a'*(16-i)
        cipher = remote_encrypt(string_sent)[:32+k*32]
        print('string sent: ', string_sent)
        for c in range(256):
            tmp = string_sent + flag + b + chr(c)
            tmp_cipher = remote_encrypt(tmp)[:32+k*32]

            if tmp_cipher == cipher and chr(c) in string.printable and c != 10 and c != 0:
                print(chr(c), c)
                b += chr(c)
                break
        flag += b
print(flag)
