#!/usr/bin/python3
# coding:utf-8

import zlib
import struct
import binascii


def crc():
    fp = '/tmp/a.png'
    with open(fp, 'rb') as f:
        ab = f.read()
    crc32_orig = int(ab[29:33].hex(), 16)
    print("crc =", crc32_orig)
    # 爆破上限，可修改
    n = 2048
    for w in range(n):
        for h in range(n):
            data = ab[12:16] + struct.pack('>i', w) + struct.pack(
                '>i', h) + ab[24:29]
            crc32 = zlib.crc32(data)
            if crc32 == crc32_orig:
                print("w =", w)
                print("h =", h)
                break


def idat():
    idat = '789C5D91011280400802BF04FFFF5C75294B5537738A21A27D1E49CFD17DB3937A92E7E603880A6D485100901FB0410153350DE83112EA2D51C54CE2E585B15A2FC78E8872F51C6FC1881882F93D372DEF78E665B0C36C529622A0A45588138833A170A2071DDCD18219DB8C0D465D8B6989719645ED9C11C36AE3ABDAEFCFC0ACF023E77C17C7897667'
    a = binascii.unhexlify(idat)
    b = zlib.decompress(a)
    print(b)


def idat1():
    fr = open('/tmp/i.png', 'rb')
    # 96775为idat数据块起始位置(010)
    fr.seek(96775, 0)
    # 98位读取大小(010)
    s = zlib.decompress(binascii.unhexlify(fr.read(98).hex()))
    fw = open('/tmp/a', 'wb')
    fw.write(s)
    fr.close()
    fw.close()

if __name__ == '__main__':
    idat()
