import gmpy2
from Crypto.Util.number import long_to_bytes


def foo(p, q, c):
    n = p * q
    inv_p = gmpy2.invert(p, q)
    inv_q = gmpy2.invert(q, p)
    mp = pow(c, (p + 1) // 4, p)
    mq = pow(c, (q + 1) // 4, q)
    a = (inv_p * p * mq + inv_q * q * mp) % n
    b = n - int(a)
    c = (inv_p * p * mq - inv_q * q * mp) % n
    d = n - int(c)
    m = [a, b, c, d]
    for i in m:
        print(long_to_bytes(i))


p = 65428327184555679690730137432886407240184329534772421373193521144693375074983
q = 98570810268705084987524975482323456006480531917292601799256241458681800554123
c = 0x4e072f435cbffbd3520a283b3944ac988b98fb19e723d1bd02ad7e58d9f01b26d622edea5ee538b2f603d5bf785b0427de27ad5c76c656dbd9435d3a4a7cf556
foo(p, q, c)