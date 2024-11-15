#!/usr/bin/env python3

import string
import itertools    # if you want, it is not necessary

XOR_KEY='??' # can be only letters

# decrypt the message
def XORencode(message, KEY):
    rep = len(message)//len(KEY) + 1
    key = (KEY*rep)[:len(message)] # adjust the key len
    xored = ''.join([chr(ord(a) ^ ord(b)) for a,b in zip(message, key)])
    return xored

# read the file with the encrypted message
with open('/home/solgio/Desktop/CyberSecurity/Es/PreExam/the-exorcist/encrypted', 'r') as f:
    encrypted_message=f.read()


with open('/home/solgio/Desktop/CyberSecurity/Es/PreExam/the-exorcist/result', 'w') as r:    
    for k in string.ascii_letters:
        for i in string.ascii_letters:
            r.write(k)
            r.write(i)
            r.write("----------------------------------------------------------------------------------------------------------------")
            r.write(XORencode(encrypted_message, k+i))
            r.write("\n\n\n\n\n\n")
    f.close()
