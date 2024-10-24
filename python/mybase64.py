#!/usr/bin/python3
# coding:utf-8


import string
import itertools
import base64


def encode(input: str, table: str) -> str:
    old = ''
    new = []
    base = ''
    for i in input:
        # old += '{:08}'.format(int(str(bin(ord(i))).lstrip('0b')))
        old += "{:08}".format(int(bin(ord(i)).lstrip('0b')))
    for j in range(0, len(old), 6):
        new.append('{:<06}'.format(old[j:j+6]))
    for k in range(len(new)):
        base += table[int(new[k], 2)]
    pad = '=' * (len(old) % 3)
    base += pad
    return base


def decode(input: str, table: str) -> str:
    old = ''
    new = ''
    for i in range(len(input.replace('=', ''))):
        old += '{:>06}'.format(bin(table.index(input[i])).lstrip('0b'))
    old += '0' * (len(old) % 8)
    for j in range(0, len(old), 8):
        new += chr(int(old[j:j+8], 2))
    return new


def solve_stege(input: list, table: str) -> str:
    binstr = ''
    for i in input:
        j = base64.b64encode(base64.b64decode(i)).decode()
        pad = i.count("=")
        if pad > 0:
            diff = abs(table.index(str(i[-(pad+1)])) - table.index(str(j[-(pad+1)])))
            if diff > 0:
                binstr += bin(diff)[2:].zfill(pad * 2)
            else:
                binstr += '0' * pad * 2
    r = ''
    for k in range(0, len(binstr), 8):
        r += chr(int(binstr[k:k+8], 2))
    return r


def foo():
    base64_table = string.ascii_uppercase + string.ascii_lowercase + string.digits + '+/'
    c = "MyLkTaP3FaA7KOWjTmKkVjWjVzKjdeNvTnAjoH9iZOIvTeHbvD=="
    table1 = "BCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    mistr = ''
    for i in range(len(base64_table)):
        if table1.find(base64_table[i]) == -1:
            mistr += base64_table[i]
    misl = []
    for j in itertools.permutations(mistr, 4):
        misl.append(''.join(j))
    for k in misl:
        m = decode(c, 'JASGBWcQPRXEFLbCDIlmnHUVKTYZdMovwipatNOefghq56rs' + k + 'kxyz012789+/')
        if 'base64' in m:
            print(m)


if __name__ == '__main__':
    '''
    base64_table = string.ascii_uppercase + string.ascii_lowercase + string.digits + '+/'
    c = "VEhJUz==\nRkxBR3==\nSVN=\nSElEREVOLo==\nQ0FO\nWU9V\nRklORM==\nSVT=\nT1VUP4==\nRE8=\nWU9V\nS05PV9==\nQkFTRTY0P5==\nWW91bmdD\nVEhJTku=\nWU9V\nQVJF\nTk9U\nVEhBVE==\nRkFNSUxJQVI=\nV0lUSO==\nQkFTRTY0Lh==\nQmFzZTY0\naXO=\nYW==\nZ3JvdXA=\nb2b=\nc2ltaWxhcn==\nYmluYXJ5LXRvLXRleHR=\nZW5jb2Rpbme=\nc2NoZW1lc0==\ndGhhdD==\ncmVwcmVzZW50\nYmluYXJ5\nZGF0YW==\naW5=\nYW6=\nQVNDSUl=\nc3RyaW5n\nZm9ybWF0\nYnk=\ndHJhbnNsYXRpbmd=\naXS=\naW50b1==\nYT==\ncmFkaXgtNjQ=\ncmVwcmVzZW50YXRpb24u\nVGhl\ndGVybc==\nQmFzZTY0\nb3JpZ2luYXRlc8==\nZnJvbd==\nYY==\nc3BlY2lmaWN=\nTUlNRT==\nY29udGVudI==\ndHJhbnNmZXI=\nZW5jb2Rpbmcu\nVGhl\ncGFydGljdWxhct==\nc2V0\nb2b=\nNjR=\nY2hhcmFjdGVyc5==\nY2hvc2Vu\ndG+=\ncmVwcmVzZW50\ndGhl\nNjQ=\ncGxhY2UtdmFsdWVz\nZm9y\ndGhl\nYmFzZd==\ndmFyaWVz\nYmV0d2Vlbt==\naW1wbGVtZW50YXRpb25zLp==\nVGhl\nZ2VuZXJhbI==\nc3RyYXRlZ3n=\naXO=\ndG9=\nY2hvb3Nl\nNjR=\nY2hhcmFjdGVyc5==\ndGhhdA==\nYXJl\nYm90aN==\nbWVtYmVyc5==\nb2a=\nYS==\nc3Vic2V0\nY29tbW9u\ndG8=\nbW9zdM==\nZW5jb2RpbmdzLA==\nYW5k\nYWxzb8==\ncHJpbnRhYmxlLg==\nVGhpc9==\nY29tYmluYXRpb25=\nbGVhdmVz\ndGhl\nZGF0YW==\ndW5saWtlbHk=\ndG/=\nYmV=\nbW9kaWZpZWS=\naW5=\ndHJhbnNpdE==\ndGhyb3VnaN==\naW5mb3JtYXRpb26=\nc3lzdGVtcyw=\nc3VjaN==\nYXM=\nRS1tYWlsLD==\ndGhhdA==\nd2VyZQ==\ndHJhZGl0aW9uYWxseQ==\nbm90\nOC1iaXQ=\nY2xlYW4uWzFd\nRm9y\nZXhhbXBsZSw=\nTUlNRSdz\nQmFzZTY0\naW1wbGVtZW50YXRpb24=\ndXNlcw==\nQahDWiw=\nYahDeiw=\nYW5k\nMKhDOQ==\nZm9y\ndGhl\nZmlyc3Q=\nNjI=\ndmFsdWVzLg==\nT3RoZXI=\ndmFyaWF0aW9ucw==\nc2hhcmU=\ndGhpcw==\ncHJvcGVydHk=\nYnV0\nZGlmZmVy\naW4=\ndGhl\nc3ltYm9scw==\nY2hvc2Vu\nZm9y\ndGhl\nbGFzdA==\ndHdv\ndmFsdWVzOw==\nYW4=\nZXhhbXBsZQ==\naXM=\nVVRGLTcu"
    input = c.split("\n")
    r = solve_stege(input, base64_table)
    print(r)
    '''
    foo()
