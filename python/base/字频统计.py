#!/usr/bin/env python3
# coding:utf-8

from collections import Counter


def foo():
    fp = "/tmp/in.txt"
    with open(fp, 'r') as f:
        s = f.read()
    # c = Counter(s).most_common(64)
    c = Counter(s)
    print(c)
    for i in c:
        print(i[0], end="")
