import requests

url_prefix = "http://factordb.com/api?query="
def factor_n(n):
    ret = []
    url = f"{url_prefix}{str(n)}"
    _data = requests.get(url=url)
    _data = _data.json()
    factors = _data.get("factors") if _data else []
    for factor in factors:
        for i in range(factor[1]):
            ret.append(int(factor[0]))
    return ret

if __name__ == '__main__':
    n = 11616788973244169211540879051135531683500013311175857700532973853592727185033846064980717918194540453710515251945345524986932165003196804187526563112454006
    ret = factor_n(n)
    print(ret)
    phi = n - (n // ret[0])
    for i in range(1, len(ret)):
        if ret[i] != ret[i-1]:
            phi = phi - phi // ret[i]

    print(phi)