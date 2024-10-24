#!/usr/bin/python3
# -*- coding:UTF-8 -*-

import hashlib


def foo():
    flag = "flag{www_shiyanbar_com_is_very_good_"
    MD5 = "38e4c352809e150186920aac37190cbc"
    for i in range(32, 126):
        for j in range(32, 126):
            for p in range(32, 126):
                for q in range(32, 126):
                    flag1 = flag + chr(i) + chr(j) + chr(p) + chr(q) + "}"
                    m = hashlib.md5(flag1.encode(encoding="UTF-8")).hexdigest()
                    if m == MD5:
                        print(flag1)
                        exit()


if __name__ == '__main__':
    a = "人工智能也要从娃娃抓起"
    m = hashlib.md5(str(a).encode(encoding="UTF-8")).hexdigest()
    print(m)
