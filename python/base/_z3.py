from z3 import *

s = Solver()
'''
p = Int('p')
q = Int('q')
'''
p, q = Ints('p q')
s.add(
    q + q * p**3 ==
    1285367317452089980789441829580397855321901891350429414413655782431779727560841427444135440068248152908241981758331600586
)
s.add(
    p * q + q * p**2 ==
    1109691832903289208389283296592510864729403914873734836011311325874120780079555500202475594
)
if s.check() == sat:
    print(s.model())