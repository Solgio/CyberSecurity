enc_flag="RmJ6cmd1dmF0IGpydmVxIHZmIHRidmF0IGJhIG5nIGd1ciB5dm9lbmVsLiBWIHpuYW50cnEgZ2IgdW5weCB2YWdiIG4gRWhmZnZuYSBzYmV6IFYgc2JoYXEgYmEgZ3VyIHl2b2VuZWwnZiBqcm9mdmdyLiBWIGd1dmF4IGd1cmwnZXIgaGZ2YXQgZ3VyIHl2b2VuZWwgbmYgbiBwYmlyZSBzYmUgemJlciBadmFxc3lubHJlIGVyZnJuZXB1LiBW4oCZeiB0YmFhbiB0dmlyIGxiaCBndXIgcGJiZXF2YW5ncmYgYnMgZ3VyIGZycGVyZyBjbmZmbnRyLCBncnl5IFp2eHIgZ2IgcGJ6ciB1cmVyIQoKNDUuNDExMzAwMTc5NjU1MDglMkMlMjAxMS44ODc3MzA3MjkyODExMTUlMjAxOS0xNi0xOC05LTIwLTI2JTdCMjAtOC01JTIwMTYtMTItMS0xNC0xMSVFMiU4MCU5OTE5JTIwMy0xNS0xNC0xOS0yMC0xLTE0LTIwJTIwOS0xOSUyMDIwLTgtNSUyMDExLTUtMjUlN0QKCjI5NjU2QzYyNjE3NDcyNkY2NjZENkY2MzIwNzQ2NTY3MjA2NDZFNjEyMDZCNkU2OTZDMjA2NTY4NzQyMDY1NzQ3MzYxNzAyODIwNDEzOTZDNjU3ODc3NkE0MTU5NUE1OTNENzYzRjY4NjM3NDYxNzcyRjZENkY2MzJFNjU2Mjc1NzQ3NTZGNzkyRTc3Nzc3NzJGMkYzQTczNzA3NDc0NjgyMDIxNjU2OTdBNzU1MzIwNzk2QzY1NzY2RjZDMjA3OTZEMjA2NDZFNjEyMDY1NkQyMDc5NjIyMDY0NjU2RDcyNkY2NjcyNjU3MDIwNjc2RTZGNzMyMDczNzM2NTZDNjQ2RTY1MjA2RTYxMjA2NTc2NzI2NTczNjU2NDIwNzU2Rjc5MjAyQzcyNjE2NjIwNzM2OTY4NzQyMDc0NjkyMDY1NjQ2MTZEMjA2NTc2Mjc3NTZGNzkyMDY2NDkyMDIxNzM2RTZGNjk3NDYxNkM3NTc0NjE3MjY3NkU2RjQz"

#GREAT; YOU'VE CLEARED THE FIRST STEP; I HAD TO ENCRYPT THE MESSAGE TO PREVENT IT FROM BEING INTERCEPTED. CONTINUE TO DECRYPT;

file_uno = open("/home/solgio/Desktop/CyberSecurity/Es/PreExam/23_24/Str4nGer_Th1ngs/test.txt", "w")


#we need to define a method that show us the k-th most frequent character in
#a given string
from collections import Counter
def k_char(text, k):
    #use the counter
    freq = Counter(text)

    #order
    ordered = sorted(freq.items(), key=lambda x: x[1], reverse=True)

    return ordered[k][0]

def frequency(text):
    all_freq = {}
 
    for i in text:
        if i in all_freq:
            all_freq[i] += 1
        else:
            all_freq[i] = 1
 
    # printing result
    print("Count of all characters in text is :\n "+ str(all_freq))

print(frequency(enc_flag))
