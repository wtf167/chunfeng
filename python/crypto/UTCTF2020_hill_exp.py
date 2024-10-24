#!/usr/bin/env python3
# coding:utf-8


import string


c = 'wznqca{d4uqop0fk_q1nwofDbzg_eu}'
m = 'utflag'
s = string.ascii_lowercase


def getkey(a1, b1, c1, a2, b2, c2, a3, b3, c3):
    for i in range(26):
        for j in range(26):
            if (a1*i+b1*j) % 26 == c1 and (a2*i+b2*j) % 26 == c2 and (a3*i+b3*j) % 26 == c3:
                return i, j


a1 = s.index(c[0])
b1 = s.index(c[1])
c1 = s.index(m[0])
a2 = s.index(c[2])
b2 = s.index(c[3])
c2 = s.index(m[2])
a3 = s.index(c[4])
b3 = s.index(c[5])
c3 = s.index(m[4])
k11, k12 = getkey(a1, b1, c1, a2, b2, c2, a3, b3, c3)
c1 = s.index(m[1])
c2 = s.index(m[3])
c3 = s.index(m[5])
k21, k22 = getkey(a1, b1, c1, a2, b2, c2, a3, b3, c3)


# 两个一组解密
cl = list(c)
pos = 0
tl = []
while pos < len(cl):
    if cl[pos] >= 'a' and cl[pos] <= 'z':
        tl.append((pos, cl[pos], False))
    if cl[pos] >= 'A' and cl[pos] <= 'Z':
        tl.append((pos, cl[pos].lower(), True))
    if len(tl) == 2:
        m1 = s[(k11*s.index(tl[0][1]) + k12*s.index(tl[1][1])) % 26]
        cl[tl[0][0]] = m1.upper() if tl[0][2] else m1
        m2 = s[(k21*s.index(tl[0][1]) + k22*s.index(tl[1][1])) % 26]
        cl[tl[1][0]] = m2.upper() if tl[1][2] else m2
        tl = []
    pos += 1
print(''.join(cl))
