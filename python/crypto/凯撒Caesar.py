#!/usr/bin/python3
# -*- coding:UTF-8 -*-


def foo(param):
    assert (type(param) is str)
    c_chr = ''
    c_ord = 0
    for s in range(1, 25):
        for i in param:
            if i >= 'A' and i <= 'Z':
                c_ord = ord('A') + (ord(i) - ord('A') + s) % 26
                c_chr = chr(c_ord)
                print("{}".format(c_chr), end="")
            elif i >= 'a' and i <= 'z':
                c_ord = ord('a') + (ord(i) - ord('a') + s) % 26
                c_chr = chr(c_ord)
                print("{}".format(c_chr), end="")
            else:
                print(i, end="")
        print("")


if __name__ == '__main__':
    c = "Dncnoqqfliqrpgeklwmppu"
    foo(c)
