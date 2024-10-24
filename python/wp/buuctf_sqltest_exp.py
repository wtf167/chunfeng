#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib.parse
fp = '/Users/wuduo/Downloads/_tmp/data.txt'
with open(fp, 'r') as f:
    fl = f.readlines()

s = []
for i in range(627, 972):
    data = urllib.parse.unquote(fl[i]).strip()
    payload = data.split("and")[1]
    positions = payload.find("from db_flag.tb_flag  limit 0,1)), ")
    data1 = payload[positions+35:].split(",")[0]
    data2 = payload[positions+35:].split(">")[1]
    s.append([data1, data2])

for i in range(1, len(s)):
    if s[i][0] != s[i-1][0]:
        print(chr(int(s[i-1][1])), end="")
print(chr(int(s[-1][1])))
