from Crypto.Util.number import *


def decode1(cipher):
    tmp = ''
    for i in range(len(cipher)):
        a = bin(eval('0x' + cipher[i]))[2:].zfill(4)
        tmp = tmp + a[0] + a[2]
        # print(tmp)
    plain = [hex(int(tmp[i:i + 8], 2))[2:] for i in range(0, len(tmp), 8)]
    return "".join(plain)


def decode2(cipher):
    tmp = ''
    for i in range(len(cipher)):
        a = bin(eval('0x' + cipher[i]))[2:].zfill(4)
        tmp = tmp + a[1] + a[3]
        # print(tmp)
    plain = [
        hex(int(tmp[i:i + 8][::-1], 2))[2:] for i in range(0, len(tmp), 8)
    ]
    return "".join(plain)


def decode3(c):
    c = '11' + bin(int(c, 16))[2:]
    t = ''
    for i in range(len(c) // 2):
        if c[2 * i] == c[i * 2 - 1]:
            t += '1'
        else:
            t += '0'
    return int(t, 2)


if __name__ == '__main__':
    cipher = "295965569a596696995a9aa969996a6a9a669965656969996959669566a5655699669aa5656966a566a56656"
    print(decode1(cipher))
    print(decode2(cipher))
    m = decode3(cipher)
    print(long_to_bytes(m))
