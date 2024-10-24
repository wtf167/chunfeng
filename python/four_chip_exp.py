import string

mm = string.ascii_lowercase

keyspace = 'jIx8fuCylrDa}pYh5wE0g7e1GQovtB9LnUN{SFWiPmK4VRkZJH623AdzqOcsbXTM'
c = 'YYm1EEiHUR9Ntx16kjtVXFWejRBBh281JqEzJocl'
col = 4
period = 7
for i in range(len(c) // period + 1):
    period = min(period, len(c) - i*period)
    darr = []
    for j in range(period):
        try:
            t = keyspace.find(c[i*7+j])
            darr.append(t // 16)
            darr.append((t % 16) // 4)
            darr.append((t % 16) % 4)
        except:
            pass
    marr = [[0, 0, 0] for mm in range(period)]
    for a in range(3):
        for b in range(period):
            marr[b][a] = darr[a*period + b]
    for d in marr:
        mi = d[0] * 16 + d[1] * 4 + d[2]
        print(keyspace[mi], end="")
