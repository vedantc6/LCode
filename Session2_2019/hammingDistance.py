class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        xor = x^y
        dist = 0
        while xor > 0:
            xor &= (xor - 1)
            dist += 1
        return dist
