#!/usr/bin/env python
# -*- coding: utf8 -*-

import gmpy2
from Crypto.Util.number import long_to_bytes


def getd(n, e, dp):
    for i in range(1, e):
        if (dp * e - 1) % i == 0:
            if n % (((dp * e - 1) // i) + 1) == 0:
                p = ((dp * e - 1) // i) + 1
                q = n // (((dp * e - 1) // i) + 1)
                print(p)
                phi = (p - 1) * (q - 1)
                d = gmpy2.invert(e, phi) % phi
                return d

def foo(n, e, dp):
    p = gmpy2.gcd(gmpy2.powmod(2,dp*e,n)-2, n)
    q = n // p
    assert(p*q == n)
    phi = (p - 1) * (q - 1)
    d = gmpy2.invert(e, phi)
    print(d)


n = int('''
248254007851526241177721526698901802985832766176221609612258877371620580060433101538328030305219918697643619814200930679612109885533801335348445023751670478437073055544724280684733298051599167660303645183146161497485358633681492129668802402065797789905550489547645118787266601929429724133167768465309665906113
''')
e = 65537
c = int('''
140423670976252696807533673586209400575664282100684119784203527124521188996403826597436883766041879067494280957410201958935737360380801845453829293997433414188838725751796261702622028587211560353362847191060306578510511380965162133472698713063592621028959167072781482562673683090590521214218071160287665180751
''')
dp = int('''
905074498052346904643025132879518330691925174573054004621877253318682675055421970943552016695528560364834446303196939207056642927148093290374440210503657
''')
d = getd(n, e, dp)
print(d)
m = gmpy2.powmod(c, d, n)
print(long_to_bytes(m).decode())
