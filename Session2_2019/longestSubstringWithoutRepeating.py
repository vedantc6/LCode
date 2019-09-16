# O(n) solution without hash
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        ans = 1
        n = len(s)
        for i in range(n-1):
            temp = s[i]
            # print("Before: ", temp)
            for j in range(i+1, n):
                if s[j] not in temp:
                    temp += s[j]
                else:
                    break
            # print("After: ", temp)
            if len(temp) > ans:
                ans = len(temp)

        return ans

# Optimized sliding window
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        charDict = {}
        ans, i = 0, 0
        for j in range(n):
            if s[j] in charDict:
                i = max(charDict[s[j]], i)
            ans = max(ans, j-i+1)
            charDict[s[j]] = j+1
        return ans
