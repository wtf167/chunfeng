import re
with open("/tmp/dump_io.txt", "r") as f:
    c = f.read()

flag = ['|' for i in range(39)]

p = r"f1a91sH3RE%29%2C(\d+)%2C1%29%29%2F%2A%2A%2Fin%2F%2A%2A%2F%28%27(\d+)%27%29%23"
for i in (c.split("\n")[:-1]):
    r = re.compile(p).findall(i)
    if not r:
        continue
    a, b = r[0]
    flag[int(a)-1] = chr(int(b))

print("".join(flag))