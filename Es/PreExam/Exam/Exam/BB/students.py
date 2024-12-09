import numpy as np

def keygen():
    key = np.random.randint(size = 1, low = 0, high =100000000)[0]
    return key


def mixer(message, key):
    np.random.seed(key)
    code = np.random.randint(size = 1, low = 50, high =100)[0]
    return ''.join([chr(ord(x) ^ code) for x in message])


with open("/home/solgio/Downloads/Exam/Exam/BB/message.txt", "r") as file:
    cipher = file.read()

for i in range(9):
        print(mixer(cipher, i),"\n\n")
      
    