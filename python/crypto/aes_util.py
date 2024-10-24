#!/usr/bin/env python3
# coding:utf-8


from Crypto.Cipher import AES
from Crypto.Util.number import long_to_bytes
from Crypto.Util.number import bytes_to_long


def foo():
    xor = 91144196586662942563895769614300232343026691029427747065707381728622849079757
    c = b'\x8c-\xcd\xde\xa7\xe9\x7f.b\x8aKs\xf1\xba\xc75\xc4d\x13\x07\xac\xa4&\xd6\x91\xfe\xf3\x14\x10|\xf8p'
    key = long_to_bytes(xor)[:16] * 2
    iv = long_to_bytes(bytes_to_long(key) ^ xor)
    aes1 = AES.new(key, AES.MODE_CBC, iv)
    m = aes1.decrypt(c)
    print(m)


if __name__ == '__main__':
    foo()
