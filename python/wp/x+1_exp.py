#!/usr/bin/env python3
# coding:utf-8


'''
题目
[13, 12, 7, 29, 31, 86, 87, 87, 12, 91, 0, 83, 0, 10, 80, 86, 86, 1, 1, 7, 5, 0, 81, 2, 4, 1, 25, 5, 7, 10, 92, 5, 7, 5, 2, 86, 68]
'''

a = 'flag{'
for i in range(len(a)-1):
    print((ord(a[i])-0) ^ (ord(a[i+1])-1), end=" ")
print("")

c = [13, 12, 7, 29, 31, 86, 87, 87, 12, 91, 0, 83, 0, 10, 80, 86, 86, 1, 1, 7, 5, 0, 81, 2, 4, 1, 25, 5, 7, 10, 92, 5, 7, 5, 2, 86, 68]
m = [ord('f')]
for i in range(len(c)):
    t = (c[i] ^ m[i]) + 1
    m.append(t)
print("".join([chr(i) for i in m]))
