import gmpy2
import libnum

'''
p1 = libnum.invmod(p, q)
q1 = libnum.invmod(q, p)
得
n = p1 * p + q1 * q -1
'''
for i in range(10):
    p = libnum.generate_prime(1024)
    q = libnum.generate_prime(1024)
    p1 = libnum.invmod(p, q) - q
    q1 = libnum.invmod(q, p) - p
    print("p1 =", p1)
    print("q1 =", q1)
    n = p * q
    n1 = p1 * p + q1 * q - 1
    print(n1//n)
