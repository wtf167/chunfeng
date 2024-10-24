#!/usr/bin/python3
# -*- coding:UTF-8 -*-

def fib(n):
    assert n > 0, n > 0
    if n == 1:
        return ['1']
    if n == 2:
        return ['1', '1']
    a = 1
    b = 1
    r = ['1', '1']
    for i in range(3, n+1):
        a, b = b, a+b
        r.append(str(b))
    return r


if __name__ == '__main__':
    t = '1 233 3 2584 1346269 144 5 196418 21 1597 610 377 10946 89 514229 987 8 55 6765 2178309 121393 317811 46368 4181 1 832040 2 28657 75025 34 13 17711'
    c = '36968853882116725547342176952286'
    m = list('a' * 32)
    fb = fib(32)
    t = t.split(' ')
    print(fb, t)
    for i in range(32):
        m[fb.index(t[i])] = c[i]
    print("".join(m))
