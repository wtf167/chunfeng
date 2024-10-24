#!/usr/bin/env python
# -*- coding: utf8 -*-


import gmpy2
from Crypto.Util.number import long_to_bytes


def decrypt(dp, dq, p, q, c):
    invq = gmpy2.invert(q, p)
    mp = pow(c, dp, p)
    mq = pow(c, dq, q)
    m = (((mp-mq)*invq) % p) * q + mq
    return m


p = 0xf85d730bbf09033a75379e58a8465f8048b8516f8105ce2879ce774241305b6eb4ea506b61eb7e376d4fcd425c76e80cb748ebfaf3a852b5cf3119f028cc5971
q = 0xc1f34b4f826f91c5d68c5751c9af830bc770467a68699991be6e847c29c13170110ccd5e855710950abab2694b6ac730141152758acbeca0c5a51889cbe84d57
dp = 0xf7b885a246a59fa1b3fe88a2971cb1ee8b19c4a7f9c1a791b9845471320220803854a967a1a03820e297c0fc1aabc2e1c40228d50228766ebebc93c97577f511
dq = 0x865fe807b8595067ff93d053cc269be6a75134a34e800b741cba39744501a31cffd31cdea6078267a0bd652aeaa39a49c73d9121fafdfa7e1131a764a12fdb95
c = int('''
0xae05e0c34e2ba4ca3536987cc2cfc3f1f7f53190164d0ac50b44832f0e7224c6fdeebd2c91e3991e7d179c26b1b997295dc9724925ba431f527fba212703a0d14a34ce133661ae0b6001ee326303d6ccdc27dbd94e0987fae25a84f197c1535bdac9094bfb3846b7ca696b2e5082bea7bff804da275772ca05dd51b185a4fc30
''', 16)
m = decrypt(dp, dq, p, q, c)
print(long_to_bytes(m).decode())
