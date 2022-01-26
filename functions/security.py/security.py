# AES 256 encryption/decryption using pycryptodome library

from base64 import b64encode, b64decode
import hashlib
from Cryptodome.Cipher import AES  
import os
from Cryptodome.Random import get_random_bytes

# Salt pa lang ang na copy paste
def encrypt(plain_text, password):
    # generate a random saltte
    salt = b'\x9f\x13\x1f\xde\xe3\xa2+\xcf\xbd\xf8.O\xcf\x81\xca@'
    print("Salt: ", salt ,"\n")

    # use the Scrypt KDF to get a private key from the password
    private_key = hashlib.scrypt(
        password.encode(), salt=salt, n=2**14, r=8, p=1, dklen=32)
    print("Private Key: ", private_key ,"\n")

    # create cipher configtest
    cipher_config = AES.new(private_key, AES.MODE_GCM)
    print("Cipher Config: ", cipher_config ,"\n")

    # return a dictionary with the encrypted text
    cipher_text, tag = cipher_config.encrypt_and_digest(bytes(plain_text, 'utf-8'))
    print("Cipher: ", cipher_text ,"\n")
    print("Tag: ", tag ,"\n")
    return {
        'cipher_text': b64encode(cipher_text).decode('utf-8'),
        'salt': b64encode(salt).decode('utf-8'),
        'nonce': b64encode(cipher_config.nonce).decode('utf-8'),
        'tag': b64encode(tag).decode('utf-8'),
    }

def decrypt(enc_dict, password):
    # decode the dictionary entries from base64
    salt = b64decode(enc_dict['salt'])
    cipher_text = b64decode(enc_dict['cipher_text'])
    nonce = b64decode(enc_dict['nonce'])
    tag = b64decode(enc_dict['tag'])
    

    # generate the private key from the password and salt
    private_key = hashlib.scrypt(
        password.encode(), salt=salt, n=2**14, r=8, p=1, dklen=32)

    # create the cipher config
    cipher = AES.new(private_key, AES.MODE_GCM, nonce=nonce)

    # decrypt the cipher text
    decrypted = cipher.decrypt_and_verify(cipher_text, tag)

    return decrypted


def main():
    password = input("PASSWORD: ")

    # First let us encrypt secret message
    encrypted = encrypt("The secretest message here", password)
    print("Encrypted Text: " , encrypted, "\n")

    # Let us decrypt using our original password
    decrypted = decrypt(encrypted, password)

    print(bytes.decode(decrypted))

main()