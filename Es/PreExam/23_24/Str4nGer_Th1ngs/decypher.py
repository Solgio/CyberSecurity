enc_flag="RmJ6cmd1dmF0IGpydmVxIHZmIHRidmF0IGJhIG5nIGd1ciB5dm9lbmVsLiBWIHpuYW50cnEgZ2IgdW5weCB2YWdiIG4gRWhmZnZuYSBzYmV6IFYgc2JoYXEgYmEgZ3VyIHl2b2VuZWwnZiBqcm9mdmdyLiBWIGd1dmF4IGd1cmwnZXIgaGZ2YXQgZ3VyIHl2b2VuZWwgbmYgbiBwYmlyZSBzYmUgemJlciBadmFxc3lubHJlIGVyZnJuZXB1LiBW4oCZeiB0YmFhbiB0dmlyIGxiaCBndXIgcGJiZXF2YW5ncmYgYnMgZ3VyIGZycGVyZyBjbmZmbnRyLCBncnl5IFp2eHIgZ2IgcGJ6ciB1cmVyIQoKNDUuNDExMzAwMTc5NjU1MDglMkMlMjAxMS44ODc3MzA3MjkyODExMTUlMjAxOS0xNi0xOC05LTIwLTI2JTdCMjAtOC01JTIwMTYtMTItMS0xNC0xMSVFMiU4MCU5OTE5JTIwMy0xNS0xNC0xOS0yMC0xLTE0LTIwJTIwOS0xOSUyMDIwLTgtNSUyMDExLTUtMjUlN0QKCjI5NjU2QzYyNjE3NDcyNkY2NjZENkY2MzIwNzQ2NTY3MjA2NDZFNjEyMDZCNkU2OTZDMjA2NTY4NzQyMDY1NzQ3MzYxNzAyODIwNDEzOTZDNjU3ODc3NkE0MTU5NUE1OTNENzYzRjY4NjM3NDYxNzcyRjZENkY2MzJFNjU2Mjc1NzQ3NTZGNzkyRTc3Nzc3NzJGMkYzQTczNzA3NDc0NjgyMDIxNjU2OTdBNzU1MzIwNzk2QzY1NzY2RjZDMjA3OTZEMjA2NDZFNjEyMDY1NkQyMDc5NjIyMDY0NjU2RDcyNkY2NjcyNjU3MDIwNjc2RTZGNzMyMDczNzM2NTZDNjQ2RTY1MjA2RTYxMjA2NTc2NzI2NTczNjU2NDIwNzU2Rjc5MjAyQzcyNjE2NjIwNzM2OTY4NzQyMDc0NjkyMDY1NjQ2MTZEMjA2NTc2Mjc3NTZGNzkyMDY2NDkyMDIxNzM2RTZGNjk3NDYxNkM3NTc0NjE3MjY3NkU2RjQz"
t = "" 
key="NREAT"

file_uno = open("/home/solgio/Desktop/CyberSecurity/Es/PreExam/23_24/Str4nGer_Th1ngs/test.txt", "w")

all_freq = {}
 

def splitter(text, key_length):
    res = []
    for i in range(key_length):
        res.append(text[i::key_length])

    return res

secret_ = splitter(enc_flag, 5)

#we need to define a method that show us the k-th most frequent character in
#a given string
from collections import Counter
def k_char(text, k):
    #use the counter
    freq = Counter(text)

    #order
    ordered = sorted(freq.items(), key=lambda x: x[1], reverse=True)

    return ordered[k][0]

## we can now see the top N freuqent words
# print(k_char(secret, 0))

#we now work on the Cryptoanalysis, based on each column of the matrix M[secret//8 X 8]
#we can first assume that the most common character in each column is the space ' '.
key_sec = [k_char(secret_[0], 0), k_char(secret_[1], 0), k_char(secret_[2], 0), k_char(secret_[3], 0),
    k_char(secret_[4], 0)]

print(key_sec)
#xor the key
real_key = [ord(k) ^ ord(' ') for k in key_sec]
print(real_key)
#decode the secret
real_message = ''
for i, c in enumerate(enc_flag):
    key_pos = i % 5
    real_message+= chr(ord(c) ^ real_key[key_pos])

print(real_message)


flag = ''.join([chr(ord(x) ^ ord(y))for x, y in zip(enc_flag, key,)])

file_uno.write(flag)