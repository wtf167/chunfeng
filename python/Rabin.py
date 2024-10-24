#!/usr/bin/python3
# coding:utf-8


import gmpy2


def rabin(p, q, c):
    n = p * q
    inv_p = gmpy2.invert(p, q)
    inv_q = gmpy2.invert(q, p)
    mp = gmpy2.powmod(c, (p + 1) // 4, p)
    mq = gmpy2.powmod(c, (q + 1) // 4, q)
    a = (inv_p * p * mq + inv_q * q * mp) % n
    b = n - int(a)
    c = (inv_p * p * mq - inv_q * q * mp) % n
    d = n - int(c)
    return a, b, c, d


if __name__ == '__main__':
    p = 49123
    q = 10663
    c = 162853095

    ml = rabin(p, q, c)
    for i in ml:
        if str(bin(i))[2:].endswith("110001"):
            print(bin(i))
