#!/usr/bin/python3
# coding:utf-8


import string
import itertools


def gen_table(key: str) -> dict:
    assert(len(key) == 5)
    t = string.ascii_lowercase.replace("j", "")
    r = {}
    for i in range(len(key)):
        for j in range(len(key)):
            r[key[i]+key[j]] = t[i*5+j]
    return r


if __name__ == '__main__':
    c = "ouauuuoooeeaaiaeauieuooeeiea"
    for i in itertools.permutations('aeiou', 5):
        t = gen_table("".join(i))
        for j in range(0, len(c), 2):
            print(t.get(c[j:j+2]), end="")
        print()
