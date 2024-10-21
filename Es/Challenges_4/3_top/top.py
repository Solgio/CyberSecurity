#!/usr/bin/env python3
import random
import sys
import time

cur_time = str(time.time()).encode('ASCII')
#random.seed(cur_time)
# msg = input('Your message: ').encode('ASCII')
# key = [random.randrange(256) for _ in msg]
# c = [m ^ k for (m,k ) in zip(msg + cur_time, key + [0x88]*len(cur_time))]

#with open(sys.argv[1], "wb") as f:
 #   f.write(bytes(c))

####--------RESOLUTION -----------------
#we know that |msg| = |key|, and |cur_time| = |[0x88]|
#we can use the xor property to retrieve the cur_time of the execution

#read the secret
with open("C:\\Users\\loren\\OneDrive\\Desktop\\Uni\\II_anno\\CyberSecurity\\Es\\Challenges_4\\3_top\\top_secret", "rb") as f:
    secret = f.read()
print(len(secret))

#extract the encrypted current time
sec_time = secret[-len(cur_time):]      #extract the last len(cur_time) bytes
plain_time = ''.join([chr(m ^ k) for (m, k) in zip(sec_time, [0x88]*len(cur_time))])
print(f"plain time:\t{plain_time}")
#what we printed seems a correct datatime format

#we now leverage on the pseudonumber vulnerabilities ...
#the algorithm set a seed, so it is not random the generator.
random.seed(plain_time.encode("ASCII"))

#get the keys                             
keys_secret = [random.randrange(256) for _ in secret[:-len(cur_time)]]  #(from beginning to len(secret) - len(cur_time))
plain_text = ''.join([chr(m ^ k) for (m, k) in zip(secret[:-len(cur_time)], keys_secret)])
print(plain_text)
