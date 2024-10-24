#!/usr/bin/env python3
# coding:utf-8

import Crypto.Util.strxor as xo
import codecs
import numpy as np


def isChr(x):
    if ord('a') <= x and x <= ord('z'):
        return True
    if ord('A') <= x and x <= ord('Z'):
        return True
    return False


def infer(index, pos):
    if msg[index, pos] != 0:
        return
    msg[index, pos] = ord(' ')
    for x in range(len(c)):
        if x != index:
            msg[x][pos] = xo.strxor(c[x], c[index])[pos] ^ ord(' ')


def getSpace():
    for index, x in enumerate(c):
        res = [xo.strxor(x, y) for y in c if x != y]
        f = lambda pos: len(list(filter(isChr, [s[pos] for s in res])))
        # cnt = [f(pos) for pos in range(len(x))]
        for pos in range(len(x)):
            dat.append((f(pos), index, pos))


c = [codecs.decode(x.strip().encode(), 'hex') for x in open('/tmp/Problem.txt', 'r').readlines()]
msg = np.zeros([len(c), len(c[0])], dtype=int)
dat = []
getSpace()
dat = sorted(dat)[::-1]
for w, index, pos in dat:
    infer(index, pos)

# print('\n'.join([''.join([chr(c) for c in x]) for x in msg]))


def know(index, pos, ch):
    msg[index, pos] = ord(ch)
    for x in range(len(c)):
        if x != index:
            msg[x][pos] = xo.strxor(c[x], c[index])[pos] ^ ord(ch)


know(10, 21, 'y')
know(8, 14, 'n')

print('\n'.join([''.join([chr(c) for c in x]) for x in msg]))
key = xo.strxor(c[0], ''.join([chr(x) for x in msg[0]]).encode())
print(key)
