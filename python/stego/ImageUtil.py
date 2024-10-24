#!/usr/bin/python3
# coding:utf-8

from PIL import Image
import matplotlib.pyplot as plt
from gmpy2 import iroot
import numpy
import binascii


def foo():
    fp = '/Users/wuduo/Downloads/tmp/flag.txt'
    with open(fp, 'r') as f:
        str = f.read()
    max = iroot(len(str), 2)[0]
    assert(iroot(len(str), 2)[1])
    pic = Image.new("RGB", (max, max))
    i = 0
    for x in range(max):
        for y in range(max):
            if (str[i] == '1'):
                pic.putpixel([x, y], (0, 0, 0))
            else:
                pic.putpixel([x, y], (255, 255, 255))
            i += 1

    pic.show()
    pic.save("/Users/wuduo/Downloads/tmp/flag.png")


def lsb(fp):
    img = Image.open(fp)
    img1 = img.copy()
    pix = img1.load()
    width, height = img1.size
    for w in range(width):
        for h in range(height):
            if pix[w, h] & 1 == 0:
                pix[w, h] = 0
            else:
                pix[w, h] = 255
    img1.show()


def plot():
    with open('/tmp/in', 'rb') as fr:
        s = binascii.unhexlify(fr.read()).decode()
        s1 = [x.lstrip('(').rstrip(')') for x in s.split('\n')]
    with open('/tmp/out', 'wb') as fw:
        fw.write('\n'.join(s1).encode())

    x, y = numpy.loadtxt('/tmp/out', delimiter=',', unpack=True)
    plt.plot(x, y, '.')
    plt.savefig('/tmp/out.png')
    plt.show()


if __name__ == '__main__':
    plot()
