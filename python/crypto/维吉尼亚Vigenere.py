#!/usr/bin/python3
# coding:utf-8

import string


def dec_key(m: str, c: str, t: str):
    key = ''
    for i in range(len(m)):
        key += t[(t.find(c[i]) - t.find(m[i])) % len(t)]
    return key


def decrypt(c: str, key: str, t: str):
    m = ''
    a = 0
    for i in range(len(c)):
        if t.find(c[i]) != -1:
            m += t[(t.find(c[i]) - t.find(key[a % len(key)])) % 26]
            a += 1
        else:
            m += c[i]
    return m


if __name__ == '__main__':
    key = 'crypto'
    c = "3ew1914zq4y48re9vc5331p15t9r8hw2"
    t = string.ascii_lowercase
    m = decrypt(c, key, t)
    print(m)
