import re
import base64


def judge_decode(s):
    if re.match("^[0-9A-F]+$", s) is not None:
        return base64.b16decode(s.encode())
    if re.match("^[A-Z2-7=]+$", s) is not None:
        return base64.b32decode(s.encode())
    if re.match("^[a-zA-Z0-9+/=]+$", s) is not None:
        return base64.b64decode(s.encode())
    print(s)
    return base64.b85decode(s.encode())


with open("/tmp/in", "r") as f:
    s = f.read()

while 1:
    if "{" in s and "}" in s:
        print(s)
        break
    s = judge_decode(s).decode()
