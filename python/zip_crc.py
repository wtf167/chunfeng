#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import string
import zipfile
import binascii


chars = string.ascii_letters + string.digits + '+/='


def crc32(crc_value):
    for c1 in chars:
        for c2 in chars:
            for c3 in chars:
                for c4 in chars:
                    for c5 in chars:
                        for c6 in chars:
                            c = c1 + c2 + c3 + c4 + c5 + c6
                            crc1 = binascii.crc32(c.encode())
                            if crc1 == crc_value:
                                return c


def get_crc():
    fp = "/tmp/a.zip"
    zf = zipfile.ZipFile(fp, mode="r")
    for ff in zf.filelist:
        print(ff.filename, ff.file_size, hex(ff.CRC))
    # crc_value = zf.filelist[2].CRC
    zf.close()

get_crc()
