class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        if n < 5:
            return 0
        i = 5
        while n//i > 0:
            count += n//i
            i *= 5
        return count
            
