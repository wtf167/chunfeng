def sbox(key):
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]
    return S
 
def prga(S):
    i, j = 0, 0
    while True:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        K = S[(S[i] + S[j]) % 256]
        yield K


def RC4(key, text):
    S = sbox(key)
    keystream = prga(S)
    res = []
    for char in text:
        res.append(char ^ next(keystream))
    return bytes(res)

if __name__ == '__main__':
    k = b"JumP1n9"
    """
    m = b"this_is_message"
    c = RC4(k, m)
    print(c)
    """
    c = "3B064BBAF18889BE76A8"
    c = bytes.fromhex(c)
    m1 = RC4(k, c)
    print(m1)
