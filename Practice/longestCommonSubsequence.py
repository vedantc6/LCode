def longestCommonSubsequence(X, Y, m, n):
    if m == 0 or n == 0:
        return 0
    elif X[m-1] == Y[n-1]:
        return (1 + longestCommonSubsequence(X, Y, m-1, n-1))
    else:
        return max(longestCommonSubsequence(X, Y, m-1, n),
        longestCommonSubsequence(X, Y, m, n-1))

X = "AGGTAB"
Y = "GXTXAYB"
print("Length of longest common subsequence in {} and {} is: {}".format(X, Y, longestCommonSubsequence(X, Y, len(X), len(Y))))
