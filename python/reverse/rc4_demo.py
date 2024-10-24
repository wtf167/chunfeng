# -*- coding:UTF-8 -*-

from Crypto.Cipher import ARC4

def dec1():
    c = [
        0x8D, 0x6C, 0x85, 0x76, 0x32, 0x72, 0xB7, 0x43, 0x85, 0x7B, 0x85, 0xDE,
        0xC1, 0xFB, 0x2E, 0x64, 0x07, 0xC8, 0x5F, 0x9A, 0x35, 0x18, 0xAD, 0xB5,
        0x15, 0x92, 0xBE, 0x1B, 0x88
    ]
    c = bytes(c)
    k = b"litctf"
    rc4 = ARC4.new(k)
    m = rc4.decrypt(c)
    print(m.decode())
    c = hex(int.from_bytes(c, "big"))
    print(c)

def enc1():
    m = "abc"
    k = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    rc4 = ARC4.new(bytes(k, "utf-8"))
    c = rc4.encrypt(m.encode())
    print(c)

def dec2():
    k = "tikpmvmbq"
    k = [ord(k[i]) ^ i for i in range(9)]
    k = "".join([chr(x) for x in k])

    s_box = list(range(256))
    j = 0
    for i in range(256):
        j = (j + s_box[i] + ord(k[i % len(k)])) % 256
        s_box[i], s_box[j] = s_box[j], s_box[i]

    c = [0xED, 0xDC, 0xC7, 0xD1, 0xD1, 0x09, 0xD4, 0x70, 0xCE, 0x24, 
         0xA1, 0xBD, 0xA6, 0xED, 0x67, 0x48, 0x63, 0xCA, 0xE6, 0x15, 
         0x04, 0xD9, 0x72, 0x43, 0x69, 0x14, 0xDC, 0xA1, 0x4C, 0x9C, 
         0xCB, 0x5E, 0x56, 0x33, 0x5C, 0x51, 0x44, 0xD3]

    i = j = 0
    m = []
    for s in c:
        i = (i + 1) % 256
        j = (j + s_box[i]) % 256
        s_box[i], s_box[j] = s_box[j], s_box[i]
        t = (s_box[i] + s_box[j]) % 256
        k = s_box[t]
        m.append(s ^ k)
    print("".join([chr(x) for x in m]))

dec2()