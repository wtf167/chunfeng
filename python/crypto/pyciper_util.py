#!/usr/bin/env python3
# coding:utf-8


from pycipher import PolybiusSquare


def polybius():
    ps = PolybiusSquare()
    m = 'aaa'
    c = ps.encipher(m)
    print(c)


if __name__ == '__main__':
    polybius()
