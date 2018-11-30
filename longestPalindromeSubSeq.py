class Solution:
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        L = [[0 for x in range(n)] for x in range(n)]

        for i in range(n):
            L[i][i] = 1

        for cl in range(2, n+1):
            for i in range(n-cl+1):
                j = i+cl-1
                if s[i] == s[j] and cl == 2:
                    L[i][j] = 2
                elif s[i] == s[j]:
                    L[i][j] = L[i+1][j-1] + 2
                else:
                    L[i][j] = max(L[i][j-1], L[i+1][j]);

        return L[0][n-1]

class Solution:
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        s2 = s[::-1]
        n = len(s)
        if not s:
            return 0
        if n == 1:
                return 1

        R = [[-1]*(n+1) for i in range(n+1)]

        for i in range(n+1):
            for j in range(n+1):
                if i==0 or j==0:
                    R[i][j] = 0
                elif s[i-1] == s2[j-1]:
                    R[i][j] = R[i-1][j-1] + 1
                else:
                    R[i][j] = max(R[i-1][j], R[i][j-1])
        return R[n][n]
