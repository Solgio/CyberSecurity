import base64

def hex2dec(text):
    res = []
    for i in range(len(text)//2):
        #get the current pair of hex
        curr = text[i*2:(i+1)*2]

        #convert to int
        res.append(int(curr, 16))

    return res

def dec2hex(text):
    return ''.join([hex(x)[2:] for x in text])

def base642ascii(text):
    res=base64.b64decode(text).decode('ascii')
    return res

def ascii2base64(text):
    text_bytes = text.encode('ascii')
    base64_bytes = base64.b64encode(text_bytes)
    base64_text = base64_bytes.decode('ascii')
    return base64_text

def dec2ascii(text):
    return ''.join([chr(x) for x in text])

def ascii2dec(text):
    return [ord(x) for x in text]

#TESTING AREA

#Test hex2dec
print("4276803= ",hex2dec("414243"))
#Test dec2hex
print("41, 42, 43 = ",dec2hex([65, 66, 67]))
#Test base642dec
print("ABC = ",base642ascii("QUJD"))
#Test ascii2base64
print("QUJD = ",ascii2base64("ABC"))
#Test dec2ascii
print("ABC = ",dec2ascii([65, 66, 67]))
#Test ascii2dec
print("65, 66, 67 = ",ascii2dec("ABC"))

