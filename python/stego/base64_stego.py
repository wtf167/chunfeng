import base64
import string


def diff(s1: str, s2: str):
    s = string.ascii_uppercase + string.ascii_lowercase + string.digits + '+/'
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return abs(s.index(s1[i]) - s.index(s2[i]))
    return 0


def base64_stego_decode(b64_str_list):
    x = ''
    for b64_str in b64_str_list:
        b64_str1 = base64.b64encode(base64.b64decode(b64_str)).decode()
        d = diff(b64_str, b64_str1)
        n = b64_str.count('=')
        if d:
            x += bin(d)[2:].zfill(n * 2)
        else:
            x += '0' * n * 2
    print(x)

    i = 0
    flag = ''
    while i < len(x):
        if int(x[i:i + 8], 2):
            flag += chr(int(x[i:i + 8], 2))
        i += 8
    print(flag)


if __name__ == '__main__':
    with open('/tmp/in', 'r') as f:
        b64_str_list = f.read().split('\n')
    base64_stego_decode(b64_str_list)
