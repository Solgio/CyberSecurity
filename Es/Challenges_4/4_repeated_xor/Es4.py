with open("C:\\Users\\loren\\OneDrive\\Desktop\\Uni\\II_anno\\CyberSecurity\\Es\\Challenges_4\\4_repeated_xor\\encrypted.txt", "rb") as f:
    secret = f.read()
print(secret)

#convertion to hex
secret_ascii = ''.join([chr(int(''.join(c))) for c in zip(secret[0::2],secret[1::2])]).replace(';', '\n- ')
 
print(secret_ascii)