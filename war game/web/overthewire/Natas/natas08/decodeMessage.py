import binascii
import base64

message = '3d3d516343746d4d6d6c315669563362'

# convert hex2bin and remove b"" in result
convert_hex_to_bin = binascii.unhexlify(message).decode('utf-8')

# reversed string 
reversed = ''.join(reversed(convert_hex_to_bin))

# base64 decode
plaintext = base64.b64decode(reversed).decode('utf-8')

print(plaintext)