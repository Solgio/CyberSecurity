def ceaser_cypher(text, n):
    res = []
    for i in range(len(text)):
        #get the current char
        curr = text[i]
        
        #convert to int
        res.append(chr(ord(curr) + n))
        
    return ''.join(res)
