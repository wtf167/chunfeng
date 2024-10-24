# -*- coding:utf-8 -*-
from randcrack import RandCrack
from hashlib import md5


with open("/tmp/random.txt", "r") as f:
    lines = f.read().strip()
s = [int(x) for x in lines.splitlines()]

rc = RandCrack()

for i, x in enumerate(s):
    if (i % 3) == 0:
        rc.submit(x)
    elif (i % 3) == 1:
        rc.submit(x % (2**32))
        rc.submit(x // (2**32))
    elif (i % 3) == 2:
        rc.submit(x % (2**64))
        rc.submit(x // (2**32) % (2**32))
        rc.submit(x // (2**64))

print(md5(str(rc.predict_getrandbits(32)).encode()).hexdigest())
