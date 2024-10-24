import gmpy2
from gmpy2 import gcd
from sympy import nextprime
from libnum import invmod
from Crypto.PublicKey import RSA
from Crypto.Util.number import long_to_bytes
from Crypto.Util.number import getPrime
from Crypto.Util.number import isPrime
from Crypto.Util.number import getRandomNBitInteger


def a(p, q, e, c):
    n = p * q
    phi = (p - 1) * (q - 1)
    d = invmod(e, phi)
    m = pow(c, d, n)
    return m


def read_public_key():
    with open("/tmp/pubkey.pem", "rb") as f:
        key = RSA.import_key(f.read())
        print('n = %d' % key.n)
        print('e = %d' % key.e)


def foo():
    n1 = 10285341668836655607404515118077620322010982612318568968318582049362470680277495816958090140659605052252686941748392508264340665515203620965012407552377979
    e = 41221
    n2 = 8559553750267902714590519131072264773684562647813990967245740601834411107597211544789303614222336972768348959206728010238189976768204432286391096419456339
    e = 41221
    c1 = 4314251881242803343641258350847424240197348270934376293792054938860756265727535163218661012756264314717591117355736219880127534927494986120542485721347351
    c2 = 485162209351525800948941613977942416744737316759516157292410960531475083863663017229882430859161458909478412418639172249660818299099618143918080867132349
    p = gcd(n1, n2)
    q1 = n1 // p
    q2 = n2 // p
    phi1 = (p - 1) * (q1 - 1)
    phi2 = (p - 1) * (q2 - 1)
    d1 = invmod(e, phi1)
    d2 = invmod(e, phi2)
    m1 = pow(c1, d1, n1)
    m2 = pow(c2, d2, n2)
    print(long_to_bytes(m1).decode(), end="")
    print(long_to_bytes(m2).decode())
