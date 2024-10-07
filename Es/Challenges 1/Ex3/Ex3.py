import random

password=[]

for i in range (10):
    num=(random.randint(33,126))
    password.append(chr(num))

    
password=''.join(password)
print(password)