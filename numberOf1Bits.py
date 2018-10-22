class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        counts = 0
        while n >= 1:
            if n % 2 != 0:
                counts += 1
            n = n//2
        return counts
            
