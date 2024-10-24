#!/usr/bin/python3

from PIL import Image
import stepic


def encode():
    fp = '/Users/wuduo/Downloads/tmp/src.jpg'
    fp2 = '/Users/wuduo/Downloads/tmp/dst.jpg'
    im = Image.open(fp)
    im2 = stepic.encode(im, "flag{this_is_flag}")
    im2.save(fp2)


def decode():
    fp = '/Users/wuduo/Downloads/tmp/hidden.jpg'
    im = Image.open(fp)
    t = stepic.decode(im)
    print(t)


if __name__ == '__main__':
    decode()
