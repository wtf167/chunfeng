from pwn import *

context(os = "linux", arch = "amd64", log_level= "error")

ip = "192.168.0.2"
port = 30297

p = remote(ip, port)

a = p.recvline()
a = p.recvline()
while True:
    a = p.recv(numb=4096)
    print(a)
    b = a.decode().split("\n")[1].replace("=", "")
    time.sleep(0.1)
    try:
        c = eval(b)
    except:
        p.interactive()
    c = eval(b)
    p.sendline(str(c))
    time.sleep(0.1)
