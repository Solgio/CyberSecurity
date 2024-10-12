s="}{[l^KlwOmwZjmOKW9"
t = "" 

file_uno = open("C:\\Users\\loren\\OneDrive\\Desktop\\Uni\\2° anno\\CyberSecurity\\Es\\Challenges 3\\1_julius\\Senza titolo.txt", "w")

for i in range (128):
    for s_elements in s:
        x=ord(s_elements)
        x=(((x+i)%128))
        t+=chr(x)

    file_uno.write(t+"\n")
    t=""

file_uno.close()