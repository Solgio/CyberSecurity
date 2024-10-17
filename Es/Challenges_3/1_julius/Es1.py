s="}{[l^KlwOmwZjmOKW9"
t = "" 

file_uno = open("C:\\Users\\loren\\OneDrive\\Desktop\\Uni\\II_anno\\CyberSecurity\\Es\\Challenges_3\\1_julius\\Senza titolo.txt", "w")

for i in range (128):
    for s_elements in s:
        x=ord(s_elements)
        x=(((x+i)%128))
        t+=chr(x)

    file_uno.write(t+"\n")
    t=""

file_uno.close()