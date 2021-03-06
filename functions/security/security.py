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
    key = str.encode(r'me%sQ%xs6rn4MWMYs4!&5Qhsh%VbZ^6d')
    iv = str.encode(r'2&4HSYK9RKk$$Bzu') #ginagawa nyang byte
    cipher = AES.new(key, AES.MODE_CBC, iv= iv)
    ct_bytes = cipher.encrypt(pad(unsecuredData, AES.block_size))

    ct = b64encode(ct_bytes).decode('utf-8') # base63 -> of that base64 ... String

    # result = {'secured_data':ct}
    return ct # MAP

def decrypt(b64Agadito): # ! JSON with base64 value in, JSON real value out
    key = str.encode(r'me%sQ%xs6rn4MWMYs4!&5Qhsh%VbZ^6d')
    iv = str.encode(r'2&4HSYK9RKk$$Bzu') #ginagawa nyang byte
    # fromSam = str.encode("UgEtBVfUpQGEQG7CcN6mRA==") #magiging byte
    try:
        # b64 = json.loads(enc_dict)
        print(b64Agadito)
        ct = b64decode(b64Agadito)
        # print(ct)
        # print(b64Agadito)
        # print(ct)
        # print('Hello') #dapat parehas sa baba
        # print(ct) #dapat parehas sa baba
        # print(b64Agadito) #parehas sa laman ng cipher
        # newSam  = b64decode(fromSam)
        # print(newSam)
        # ct = fromSam #base64 text
        cipher = AES.new(key, AES.MODE_CBC, iv)
        pt = unpad(cipher.decrypt(ct), AES.block_size)
        # print("The message was: ", pt.decode('utf-8')) # String value
        print('\n\n\nPT VALUE ::: ') #base 64
        print(pt) #base 64
        return pt.decode('utf-8') #returns String
        # return pt

    except (ValueError, KeyError):
        print("Incorrect decryption")
