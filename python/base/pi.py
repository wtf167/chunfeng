def pi(n):
    dbPiTmp = 1.0
    for i in range(1, n, 2):
        dbPiTmp = dbPiTmp - 1/(2*i+1) + 1/(2*(i+1)+1)
    return dbPiTmp * 4

print(pi(1000000))