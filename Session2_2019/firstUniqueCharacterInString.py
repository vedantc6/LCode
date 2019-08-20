class Solution:
    def firstUniqChar(self, s: str) -> int:
        charDict = {}
        ans = []
        for c in s:
            if c not in charDict:
                charDict[c] = 1
                ans.append(c)
            else:
                charDict[c] += 1

        for key, val in charDict.items():
            if val != 1:
                ans.remove(key)

        if not ans:
            return -1
        return s.index(ans[0])
