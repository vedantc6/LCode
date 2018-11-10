def editDistance(x, y):
    m = len(x)
    n = len(y)
    E = [[0 for j in range(n+1)] for i in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i==0:
                E[0][j] = j
            elif j==0:
                E[i][0] = i
            elif x[i-1]==y[j-1]:
                E[i][j] = E[i-1][j-1]
            else:
                E[i][j] = min(E[i-1][j], E[i][j-1], E[i-1][j-1]) + 1

    return E[m][n]

s1 = "snowy"
s2 = "sunny"
print(editDistance(s1, s2))
