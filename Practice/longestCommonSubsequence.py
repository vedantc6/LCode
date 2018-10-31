# Through normal recursion
def longestCommonSubsequence(X, Y, m, n):
    if m == 0 or n == 0:
        return 0
    elif X[m-1] == Y[n-1]:
        return (1 + longestCommonSubsequence(X, Y, m-1, n-1))
    else:
        return max(longestCommonSubsequence(X, Y, m-1, n),
        longestCommonSubsequence(X, Y, m, n-1))

# Through memoization
def longestCommonSubsequenceM(X, Y, m, n, L):
    if m == 0 or n == 0:
        return 0
    if L[m-1][n-1] != -1:
        return L[m-1][n-1]
    elif X[m-1] == Y[n-1]:
        L[m-1][n-1] = 1 + longestCommonSubsequenceM(X, Y, m-1, n-1, L)
        return L[m-1][n-1]
    else:
        L[m-1][n-1] = max(longestCommonSubsequenceM(X, Y, m-1, n, L),
        longestCommonSubsequenceM(X, Y, m, n-1, L))
        return L[m-1][n-1]

# Through dynamic programming
def longestCommonSubsequenceDP(X, Y, m, n):
    R = [[-1]*(n+1) for i in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                R[i][j] = 0
            elif X[i-1] == Y[j-1]:
                R[i][j] = 1 + R[i-1][j-1]
            else:
                R[i][j] = max(R[i-1][j], R[i][j-1])

    return R[m][n]

X = "AGGTABUOGSFOGWF"
Y = "GXTXAYBDSHODWG"
m = len(X)
n = len(Y)
L = [[-1]*(n+1)  for i in range(m+1)]

print("Length of longest common subsequence in {} and {} is: {}".format(X, Y, longestCommonSubsequence(X, Y, m, n)))
print("Length of longest common subsequence in {} and {} is: {}".format(X, Y, longestCommonSubsequenceM(X, Y, m, n, L)))
print("Length of longest common subsequence in {} and {} is: {}".format(X, Y, longestCommonSubsequenceDP(X, Y, m, n)))
