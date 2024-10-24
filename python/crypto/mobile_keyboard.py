#!/usr/bin/env python3
# -*- coding:utf-8 -*-


dic = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]


def decrypt(c):
    flag = ""
    for i in c:
        index = int(i[0])
        pos = len(i) - 1
        flag += dic[index][pos]
    return flag


if __name__ == '__main__':
    c = "999*666*88*2*777*33*6*999*4*444*777*555*333*777*444*33*66*3*7777".split("*")
    flag = decrypt(c)
    print(flag)
