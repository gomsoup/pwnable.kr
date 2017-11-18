from pwn import *
import re

r = remote("pwnable.kr", 9007)
C = 0

def binary_search(first, last):
	global cnt
	global C
	
	s = ""
	l = []

	for i in range(first, (first+last) / 2):
		l.append(i)

	for i in l:
		s = s + " " + str(i)
	
	r.sendline(s)
	w = int(r.recv())

	if (w != len(l) * 10 ):
		if(len(l) <= 2):
			r.sendline(str(l[0]))
			w = r.recv()
			if (w == "9\n"):
				while( not("Correct" in w)):
					r.sendline(str(l[0]))
					w = r.recv()
			else:
	  			while( not("Correct" in w)):
					r.sendline(str(l[1]))
					w = r.recv()
		else:
			last = (first + last) / 2
			binary_search(first, last)
	elif(len(l) == 1):
		r.sendline(str(l[0]+1))
		w = r.recv()
		if (w == "9\n"):
			while( not("Correct" in w)):
				r.sendline(str(l[0]+1))
				w = r.recv()
		else:
			while( not("Correct" in w)):
				r.sendline(str(l[0]+2))
				w = r.recv()
	else:
		first = (first + last) / 2
		binary_search(first, last)

	
r.recvuntil("... -")
sleep(3)

r.recvuntil('\n')
r.recvuntil('\n')

print "binary searching",

while (True):
	print ".",

	data = r.recvuntil('\n')
	s = re.findall('\d+', data)
	
	if "flag" in data:
		print ""
		print "Done!!!"
		print "flag : " + r.recv()
		break

	N = int(s[0])
	C = int(s[1])
	binary_search(0, N)


