import string

t = '''1： <ZWAXJGDLUBVIQHKYPNTCRMOSFE <
2： <KPBELNACZDTRXMJQOYHGVSFUWI <
3： <BDMAIZVRNSJUWFHTEQGYXPLOCK <
4： <RPLNDVHGFCUKTEBSXQYIZMJWAO <
5： <IHFRLABEUOTSGJVDKCPMNZQWXY <
6： <AMKGHIWPNYCJBFZDRUSLOQXVET <
7： <GWTHSPYBXIZULVKMRAFDCEONJQ <
8： <NOZUTWDCVRJLXKISEFAPMYGHBQ <
9： <QWATDSRFHENYVUBMCOIKZGJXPL <
10： <WABMCXPLTDSRJQZGOIKFHENYVU <
11： <XPLTDAOIKFZGHENYSRUBMCQWVJ <
12： <TDSWAYXPLVUBOIKZGJRFHENMCQ <
13： <BMCSRFHLTDENQWAOXPYVUIKZGJ <
14： <XPHKZGJTDSENYVUBMLAOIRFCQW <'''
t = [x.split("<")[1].rstrip(" ") for x in t.split("\n")]

# 根据密钥k变换顺序
k = [2, 5, 1, 3, 6, 4, 9, 7, 8, 14, 10, 13, 11, 12]
t = [t[x - 1] for x in k]
c = 'HCBTSXWCRQGLES'
for i in range(len(c)):
    ii = t[i].index(c[i])
    t[i] = t[i][ii:] + t[i][:ii]

for i in range(len(t[0])):
    for j in range(len(t)):
        print(t[j][i].lower(), end="")
    print("")