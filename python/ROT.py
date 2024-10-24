#!/usr/bin/python3
# -*- coding:UTF-8 -*-

import string


ascii_lowercase = string.ascii_lowercase
ascii_uppercase = string.ascii_uppercase
digits = string.digits


def rot5(p):
    t = digits[5:] + digits[:5]
    for i in p:
        print(t[int(i)], end="")


def rot13(p):
    t_l = ascii_lowercase[13:] + ascii_lowercase[:13]
    t_u = ascii_uppercase[13:] + ascii_uppercase[:13]
    for i in p:
        if i >= 'a' and i <= 'z':
            print(t_l[ascii_lowercase.index(i)], end="")
        elif i >= 'A' and i <= 'Z':
            print(t_u[ascii_uppercase.find(i)], end="")
        else:
            print(i, end="")


def rot47(p):
    x = []
    for i in p:
        j = ord(i) + 47
        if j > 126:
            j = j - 126 + 32
        x.append(chr(j))
    return "".join(x)


if __name__ == '__main__':
    p = "-,'=?vww,{ s *pvv!!'% q"$!9%'*|%'%"vd"
    r = rot47(p)
    print(r)
