class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 0:
            return ""
        res = ""
        ints = '0ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        if n <= 26:
            return ints[n]
        while n > 0:
            n, r = divmod(n, 26)
            if r == 0:
                n -= 1
                r += 26
            res += ints[r]

        return (res[::-1])

# Faster
class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = ''
        if n < 0:
            return -1
        if 0 < n <= 26:
            res = chr(n + 64)
            return res
        if n > 26:
            while n > 26:
                remainder = n % 26
                if remainder == 0:
                    res = chr(64 + 26) + res
                    n = (n - 26) // 26
                else:
                    res = chr(64 + remainder) + res
                    n = (n - remainder) // 26
        res = chr(64 + n) + res
        return res
