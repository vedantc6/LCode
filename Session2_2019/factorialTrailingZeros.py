class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 5
        count = 0
        while n/i >= 1:
            count += n//i
            i = i*5
        return count