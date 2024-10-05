import random

password=[]
i=0
for i in range (10):
    num=(random.randint(33,126))
    password.append(chr(num))
    i+=1

    
password=''.join(password)
print(password)