class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        result = 0
        s = s[::-1]
        for i in range(len(s)-1,-1,-1):
            result += (ord(s[i])-65+1)*(26**i)
        return result

# SLOWER
class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        result = 0
        s = s[::-1]
        for i, char in enumerate(s):
            result += (ord(char)-64)*(26**i)
        return result
