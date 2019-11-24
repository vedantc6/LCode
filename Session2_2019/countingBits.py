# SLOW
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        result = []

        for i in range(num+1):
            count = 0
            n = i
            while n > 0:
                n &= (n-1)
                count += 1
            result.append(count)

        return result

# O(n)
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        result = [0]*(num+1)
        offset = 1
        for i in range(1, num+1):
            if i == offset*2:
                offset = offset*2
            result[i] = result[i-offset] + 1

        return result
        
