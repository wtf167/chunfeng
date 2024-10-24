# -*- coding: utf8 -*-
'''
1.x异或y = r
2.x与y = t
3.t左移1位
4.判断t t为0则r为结果 t不为0 x=r y=t 重复1到4
'''

def cpu_add(x: int, y: int):
    r = x ^ y
    t = (x & y) << 1
    while t != 0:
        x = r
        y = t
        r = x ^ y
        t = (x & y) << 1
    return r


c = cpu_add(2, -3)
print(c)
