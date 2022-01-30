# AES 256 encryption/decryption using pycryptodome library

from Crypto.Util.Padding import pad
from base64 import b64encode, b64decode
import hashlib
from Cryptodome.Cipher import AES  
import os
from Cryptodome.Random import get_random_bytes
from Crypto.Util.Padding import unpad
import json


# Salt pa lang ang na copy paste
# !str(map)
def encrypt(jsonNaString):
    unsecuredData = str.encode(jsonNaString)
    key = str.encode('my 32 length key................')
    iv = str.encode('1234567890123456') #ginagawa nyang byte
    cipher = AES.new(key, AES.MODE_CBC, iv= iv)
    ct_bytes = cipher.encrypt(pad(unsecuredData, AES.block_size))

    ct = b64encode(ct_bytes).decode('utf-8') # base63 -> of that base64 ... String

    result = {'securedB64String':ct}
    return result # MAP

def decrypt(enc_dict): # ! JSON with base64 value in, JSON real value out
    key = str.encode('my 32 length key................')
    iv = str.encode('1234567890123456') #ginagawa nyang byte

    fromSam = str.encode("UgEtBVfUpQGEQG7CcN6mRA==")

    try:
        b64 = json.loads(enc_dict)
        ct = b64decode(b64['ciphertext'])
        print('Hello') #dapat parehas sa baba
        print(ct) #dapat parehas sa baba
        # print(fromSam) #parehas sa laman ng cipher
        newSam  = b64decode(fromSam)
        print(newSam)
        # ct = fromSam #base64 text
        cipher = AES.new(key, AES.MODE_CBC, iv)
        pt = unpad(cipher.decrypt(ct), AES.block_size)
        # print("The message was: ", pt.decode('utf-8')) # String value
        # print(pt) #base 64
        return pt.decode('utf-8') #returns String

    except (ValueError, KeyError):
        print("Incorrect decryption")
