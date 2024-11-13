from Crypto.Cipher import DES
from Crypto.Util import Counter
import libnum
from itertools import product
import string

def dec(iv, key, c):
    ctr = Counter.new(64, initial_value=int.from_bytes(iv, byteorder="big"))
    des1 = DES.new(key=key, mode=DES.MODE_CTR, counter=ctr)
    m = des1.decrypt(c)
    return m

if __name__ == '__main__':
    c = "37b10cfc8ac44327618646926264dfde6609d5e64df9a1128b7ec2f3c5f58fefbfb2b3aa30b1b55524cb"
    c = bytes.fromhex(c)
    key = b"gamelab@"
    t = string.digits
    for i in product(t, repeat=4):
        a = "".join(i)
        iv = f"01{a}04"
        iv = iv.encode()
        m = dec(iv, key, c)
        if b"flag" in m:
            print(m, iv)
            break