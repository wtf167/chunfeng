#!/usr/bin/env python3
# coding:utf-8


import string


# 棋盘密码
def foo():
    s = string.ascii_lowercase.replace("j", "")
    c = "4423244324433534315412244543"
    m = []
    for i in range(0, len(c), 2):
        t = s[(int(c[i])-1) * 5 + (int(c[i+1])-1)]
        m.append(t)
    print("".join(m))


if __name__ == '__main__':
    foo()
