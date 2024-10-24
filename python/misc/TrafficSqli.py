import pyshark
import re


def foo():
    cap = pyshark.FileCapture("/tmp/a.pcapng", display_filter='http.request.uri')
    a = []    
    for pkt in cap:
        a.append(pkt[pkt.highest_layer].request_uri)
    print(len(a))

    p = r'tb_flag%20%20limit%200,1\)\),%20(\d+),%201\)\)>(\d+)'
    flag = ["-" for x in range(39)]
    for i in a:
        r = re.compile(p).findall(i)
        if r:
            x, y = r[0]
            flag[int(x)] = chr(int(y))
    print("".join(flag))

foo()
