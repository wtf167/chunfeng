# -*- coding:utf-8 -*-

import gmpy2
import libnum
import uuid

flag = "flag{" + str(uuid.uuid4()) + "}"

p = libnum.generate_prime(1024)
q = libnum.generate_prime(1024)
r = libnum.generate_prime(1024)
e = libnum.generate_prime(32)
n = p * q * r
phi = (p-1) * (q-1) * (r-1)
d = libnum.invmod(e, phi)
dp = d % ((q-1) * (r-1))
dq = d % ((p-1) * (r-1))
dr = d % ((p-1) * (q-1))
m = libnum.s2n(flag)
c = gmpy2.powmod(m, e, n)
print("p =", p)
print("q =", q)
print("r =", r)
print("dp =", dp)
print("dq =", dq)
print("dr =", dr)
print("c =", c)
print("#flag=",flag)
