import string


def foo():
    a = "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz"
    b = "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm"
    t = str.maketrans(a, b)
    c = "abcdABCD"
    m = str.translate(c, t)
    print(type(m))
    print(m)

foo()