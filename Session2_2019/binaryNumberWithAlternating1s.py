class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return (n & (n>>1) == 0) and (n & (n>>2) == n>>2)

# Faster
class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        bits = bin(n)
        return all(bits[i] != bits[i+1]
                   for i in xrange(len(bits) - 1))
