s=input()
s=list(s) 
i=0
for s_elements in s:
    x=ord(s[i])
    x=(x+9)%128
    s[i]=chr(x)
    i+=1
s=''.join(s)
print(s)