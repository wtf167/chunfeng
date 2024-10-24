import string

mm = string.ascii_lowercase

keyspace = 'jIx8fuCylrDa}pYh5wE0g7e1GQovtB9LnUN{SFWiPmK4VRkZJH623AdzqOcsbXTM'
c_r = 'YYm1EEiHUR9Ntx16kjtVXFWejRBBh281JqEzJocl'
t = keyspace.find('H')
col = 4
flag = 'DASCTF{bbbbbbb%s}' % ('b'*17)
for a1 in range(61):
    for a2 in range(61):
        for a3 in range(61):
            b1 = a1//col**2 + 1
            b2 = a2//col**2 + 1
            b3 = a3//col**2 + 1
            if ((b1-1)*col**2 + (b2-1)*col + (b3-1)) == t:
                print(a1, a2, a3)
