#!/usr/bin/python3
# coding:utf-8

import gmpy2
import string

# y =ax +b % 62
s1 = []
s = string.ascii_letters + string.digits + '{}'
print(s)

c = [13, 12, 7, 29, 31, 86, 87, 87, 12, 91, 0, 83, 0, 10, 80, 86, 86, 1, 1, 7, 5, 0, 81, 2, 4, 1, 25, 5, 7, 10, 92, 5, 7, 5, 2, 86, 68]
for a in range(2, 93):
    if gmpy2.gcd(a, 93) == 1:
        a_1 = int(gmpy2.invert(a, 93))
        for b in range(0, 93):
            m1 = []
            for i in c:
                t = s[((i + 1 - b) * a_1) % 93]
                m1.append(t)
            m = "".join(m1)
            if "f" in m and "l" in m and "a" in m and "g" in m:
                print(m)
