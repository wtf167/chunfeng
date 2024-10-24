#!/usr/bin/env python
# -*- coding: utf8 -*-


import gmpy2
import string


def decrypt(a, b, c):
    t1 = string.ascii_lowercase
    t2 = string.ascii_uppercase
    a_ = gmpy2.invert(a, 26)
    m = ""
    for i in range(len(c)):
        if c[i] >= 'a' and c[i] <= 'z':
            m += t1[((t1.index(c[i]) - b) * a_) % 26]
        elif c[i] >= 'A' and c[i] <= 'Z':
            m += t2[((t2.index(c[i]) - b) * a_) % 26]
        else:
            m += c[i]
    return m


a = 25
b = 9
c = "eyjd{4e71wf_H1uc3s_15_EEEEpwwl!!}"
m = decrypt(a, b, c)
print(m)
