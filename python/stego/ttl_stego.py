#!/usr/bin/env python3
# -*- coding:utf-8 -*-


ttl_file = "/tmp/ttl.txt"
with open(ttl_file, 'r') as f:
    a = [int(x.rstrip("\n")) for x in f.readlines()]

m = ""
for i in a:
    m += bin(i)[2:].zfill(8)[:2]
print(m)

m_str = ""
for i in range(0, len(m), 8):
    m_str += chr(int(m[i:i+8], 2))
print(m_str)
