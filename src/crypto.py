#!/usr/bin/env python3
import os
import random
import secrets
import string
try:
    import simplejson as json
except:
    import json
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from random import randint

# @author:satoshilabs
def decryptEntryValue(nonce, valArr):
    valHex = ''.join([hex(x)[2:].zfill(2) for x in valArr])
    val = bytes.fromhex(valHex)
    cipherkey = bytes.fromhex(nonce)
    iv = val[:12]
    tag = val[12:28]
    cipher = Cipher(algorithms.AES(cipherkey), modes.GCM(iv, tag), backend=default_backend())
    decryptor = cipher.decryptor()
    data = ''
    inputData = val[28:]
    while True:
        block = inputData[:16]
        inputData = inputData[16:]
        if block:
            data = data + decryptor.update(block).decode()
        else:
            break
        # throws exception when the tag is wrong
    data = data + decryptor.finalize().decode()
    return json.loads(data)

def encryptEntryValue(nonce, val, iv):
    cipherkey = bytes.fromhex(nonce)
    cipher = Cipher(algorithms.AES(cipherkey), modes.GCM(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    cipherText = encryptor.update(val.encode("utf-8", "replace")) + encryptor.finalize()
    cipherText = iv + encryptor.tag + cipherText
    return [x for x in cipherText]

# @author:satoshilabs
def decryptStorage(store_path, encKey):
    cipherkey = bytes.fromhex(encKey)
    with open(store_path, 'rb') as f:
        iv = f.read(12)
        tag = f.read(16)
        cipher = Cipher(algorithms.AES(cipherkey), modes.GCM(iv, tag), backend=default_backend())
        decryptor = cipher.decryptor()
        data = ''
        while True:
            block = f.read(16)
            if block:
                data = data + decryptor.update(block).decode()
            else:
                break
        data = data + decryptor.finalize().decode()
    return json.loads(data)

def encryptStorage(string, encKey, iv): 
    cipherkey = bytes.fromhex(encKey)
    cipher = Cipher(algorithms.AES(cipherkey), modes.GCM(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    cipherText = encryptor.update(string.encode("UTF-8", "replace")) + encryptor.finalize()
    cipherText = iv + encryptor.tag + cipherText
    return cipherText
            
def generatePassword(length):
    chars = (string.digits + string.ascii_letters + string.punctuation)
    while True:
        password = ''.join(random.choice(chars) for x in range(length))
        if (any(c.islower() for c in password)
                and any(c.isupper() for c in password)
                and sum(c.isdigit() for c in password) >= 2):
            break
    return password

def generatePassphrase(length, words, seperator):
    winners = []
    for i in range(0, int(length)):
        choose = (secrets.randbelow(6) + 1) + 10 * (secrets.randbelow(6) + 1) + 100 * (secrets.randbelow(6) + 1) + 1000 * (secrets.randbelow(6) + 1) + 10000 * (secrets.randbelow(6) + 1)
        winners.append(words[str(choose)])
    return seperator.join(winners)

def generatePin(length):
    pin = ''
    for i in range(0, int(length)):
        pin = pin + str(secrets.randbelow(10))
    return pin
