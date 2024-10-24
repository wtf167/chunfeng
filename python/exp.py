#!/usr/bin/python3
# coding:utf-8

import string
import gmpy2


best_index_of_Coincidence = 0.065

best_freq = {}
best_freq['a'] = 0.08167
best_freq['b'] = 0.01492
best_freq['c'] = 0.02782
best_freq['d'] = 0.04253
best_freq['e'] = 0.12702
best_freq['f'] = 0.02228
best_freq['g'] = 0.02015
best_freq['h'] = 0.06094
best_freq['i'] = 0.06966
best_freq['j'] = 0.00153
best_freq['k'] = 0.00772
best_freq['l'] = 0.04025
best_freq['m'] = 0.02406
best_freq['n'] = 0.06749
best_freq['o'] = 0.07507
best_freq['p'] = 0.01929
best_freq['q'] = 0.00095
best_freq['r'] = 0.05987
best_freq['s'] = 0.06327
best_freq['t'] = 0.09056
best_freq['u'] = 0.02758
best_freq['v'] = 0.00978
best_freq['w'] = 0.02360
best_freq['x'] = 0.00150
best_freq['y'] = 0.01974
best_freq['z'] = 0.00074
ascii_lowercase = string.ascii_lowercase

fp = '/Users/wuduo/Documents/ctf/a/[XNUCA2018]baby_crypto/encrypted_message'
with open(fp, 'r') as f:
    c = f.read()


def index_of_coincidence(s):
    '''
    计算字符串s的重合指数，即所有字符出现概率的平方和
    :param s:密文字符串
    :return:s的重合指数
    '''
    freq = {}
    for x in ascii_lowercase:
        freq[x] = 0
    for x in s:
        freq[x] = freq[x] + 1
    index = 0
    for x in ascii_lowercase:
        # index = index + pow(float(freq[x]) / len(s), 2)
        index = index + float(freq[x] * (freq[x] - 1)) / (len(s) * (len(s) - 1))
    return index


def index_of_coincidence_2(s):
    '''
    计算明文s的拟重合指数，即s中字母的频率与英文字母的统计规律吻合程度
    :param s:解出的明文
    :return:s的拟重合指数
    '''
    freq = {}
    for x in ascii_lowercase:
        freq[x] = 0
    for x in s:
        freq[x] = freq[x] + 1
    index = 0
    for x in ascii_lowercase:
        index = index + float(freq[x]) / len(s) * best_freq[x]
    return index


def guessMN():
    '''
    根据题意，该加密应当会周期使用密钥，该周期是key_a长度和key_k长度的最小公倍数。
    遍历周期1到100，分别测试不同周期下各个子密文段的重合指数，然后求平均
    :return:无返回值，打印出所有与最佳重合指数相差小于0.01的周期
    '''
    for x in range(1, 100):
        avergage_index = 0
        for i in range(x):
            s = ''.join([c[j * x + i] for j in range(0, len(c) // x)])
            index = index_of_coincidence(s)
            avergage_index += index

        avergage_index = avergage_index / x - best_index_of_Coincidence
        if abs(avergage_index) < 0.01:
            print('x=', x)
            print(avergage_index)


print('开始猜测周期')
guessMN()
# 结果显示，重合指数得分较高的都是6的整数倍，所以周期极有可能是6
x = 12


def decryptChar(c, i, j):
    '''
    对单个密文字符解密。
    :param c: 单个密文字符
    :param i: 与字符c相乘的那个密钥
    :param j: 用于位移的密钥
    :return: 明文字符
    '''
    i_inv = gmpy2.invert(i, 26)
    p = chr((ord(c) - ord('a') - j) * i_inv % 26 + ord('a'))
    return p


def decrypt(s, i, j):
    '''
    用固定的i和j，解密子密文段
    :param s: 使用相同i和j加密的子密文段
    :param i: 与字符c相乘的那个密钥
    :param j: 用于位移的密钥
    :return: 明文字符串
    '''
    p = ''
    for c in s:
        p += decryptChar(c, i, j)
    return p


def guessKey(c):
    '''
   对子密文段爆破它所使用的i和j
    :param c: 子密文段
    :return: 无返回值，但是打印拟重合指数最佳的i和j，即解出的明文统计规律与英文字符统计规律最吻合的i和j
    '''
    for i in range(26):
        # 若i与26不互素，则解除的明文不唯一，所以i一定不是2和13的倍数
        if i % 2 == 0 or i == 13:
            continue
        for j in range(26):
            s = decrypt(c, i, j)
            # print s
            index = index_of_coincidence_2(s)
            index = abs(index - 0.065)
            if index < 0.01:
                print(i, j, index)


def guessAllKeys():
    '''
   以l为周期，将完整密文c切分成l个子密文段，对这l个子密文段分别爆破其所使用密钥i和j
    :return: 无返回值，但打印出最佳的密钥组合
    '''
    for i in range(x):
        s = ''.join([c[j * x + i] for j in range(0, len(c) // x)])
        print(i)
        guessKey(s)


print('开始猜测密钥组合')
guessAllKeys()
# 根据打印结果，发现最佳组合依次是
# 19,10
# 7,9
# 23,3
# 19,24
# 7,14
# 23,15
# 将l设置成12、18、24或更多，还是可以得到这样的组合的重复
# 现在基本可以确定密钥应该是这样的
key_a = [19, 7, 23]
key_k = [10, 9, 3, 24, 14, 15]

# 利用key_a, key_k解密完整的密文，得到明文
p = ''
for i in range(len(c)):
    p += decryptChar(c[i], key_a[i % 3], key_k[i % 6])
print(p)
# 明文.......flagishelloxnucagoodluck
# 末尾是flagishelloxnucagoodluck
# 由此可得falg：helloxnucagoodluck
import gmpy2
import binascii
def decrypt(dp,dq,p,q,c):
	InvQ = gmpy2.invert(q,p)
	mp = pow(c,dp,p)
	mq = pow(c,dq,q)
	m=(((mp-mq)*InvQ)%p)*q+mq
	print (binascii.unhexlify(hex(m)[2:]))

p=0xf85d730bbf09033a75379e58a8465f8048b8516f8105ce2879ce774241305b6eb4ea506b61eb7e376d4fcd425c76e80cb748ebfaf3a852b5cf3119f028cc5971
q=0xc1f34b4f826f91c5d68c5751c9af830bc770467a68699991be6e847c29c13170110ccd5e855710950abab2694b6ac730141152758acbeca0c5a51889cbe84d57
dp=0xf7b885a246a59fa1b3fe88a2971cb1ee8b19c4a7f9c1a791b9845471320220803854a967a1a03820e297c0fc1aabc2e1c40228d50228766ebebc93c97577f511
dq=0x865fe807b8595067ff93d053cc269be6a75134a34e800b741cba39744501a31cffd31cdea6078267a0bd652aeaa39a49c73d9121fafdfa7e1131a764a12fdb95
c=0xae05e0c34e2ba4ca3536987cc2cfc3f1f7f53190164d0ac50b44832f0e7224c6fdeebd2c91e3991e7d179c26b1b997295dc9724925ba431f527fba212703a0d14a34ce133661ae0b6001ee326303d6ccdc27dbd94e0987fae25a84f197c1535bdac9094bfb3846b7ca696b2e5082bea7bff804da275772ca05dd51b185a4fc30

decrypt(dp,dq,p,q,c)
