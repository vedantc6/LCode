# Expand around center
class Solution:
    def expandAroundCenter(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return r - l - 1

    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) < 1:
            return ''
        start, end = 0, 0
        for i in range(len(s)):
            len1 = self.expandAroundCenter(s, i, i)
            len2 = self.expandAroundCenter(s, i, i+1)
            maxLen = max(len1, len2)
            if maxLen > end - start:
                start = i - int((maxLen-1)/2)
                end = int(i + maxLen/2)
        # print(start, end)
        return s[start:end+1]

# DP solution
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) < 1:
            return ''
        n = len(s)
        # For single characters
        results = [[1 if i == j else 0 for i in range(n)] for j in range(n)]
        maxLen = 1
        start = 0

        # For 2 characters
        for i in range(n-1):
            if s[i] == s[i+1]:
                results[i][i+1] = 1
                start = i
                maxLen = 2

        # For more than 2 characters
        for k in range(3, n+1):
            for i in range(n - k + 1):
                # End point
                j = i + k - 1
                if results[i+1][j-1] == 1 and s[i] == s[j]:
                    results[i][j] = 1
                    if k > maxLen:
                        maxLen = k
                        start = i
        return s[start:start+maxLen]
