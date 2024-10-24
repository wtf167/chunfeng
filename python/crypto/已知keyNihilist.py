import string

key1 = "lovekfc"
lc = string.ascii_lowercase
uc = string.ascii_uppercase
key2 = [x for x in lc if x not in key1]
key = key1 + "".join(key2)
tl = str.maketrans(key, lc)
tu = str.maketrans(key.upper(), uc)
c = "PVSF{vVckHejqBOVX9C1c13GFfkHJrjIQeMwf}"
m = str.translate(c, tl)
m = str.translate(m, tu)
print(m)
