#!/usr/bin/python3
# coding:utf-8

import zipfile
import datetime
import os


def extractFile(fp, f, password):
    zf = zipfile.ZipFile(os.path.join(fp, f))
    for p in password:
        try:
            zf.extractall(path=fp, members=zf.namelist(), pwd=p.encode())
            print("passwd:", p)
            return p
        except Exception:
            pass


def datelist(begin, end):
    dl = []
    for i in range((end - begin).days + 1):
        day = begin + datetime.timedelta(days=i)
        dl.append(day.strftime("%Y%m%d"))
    return dl


if __name__ == '__main__':
    fp = '/Users/wuduo/Downloads/tmp/'
    f = 'howtoencrypt.zip'
    for i in range(1999, 2000):
        begin = datetime.date(i, 1, 1)
        end = datetime.date(i, 12, 31)
        dl = datelist(begin, end)
        p = extractFile(fp, f, dl)
        if p:
            exit
