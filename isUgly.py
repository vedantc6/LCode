class Solution:
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0 or num >= 2147483648:
            return False
        while num > 1:
            # print(num)
            if num%5 == 0:
                num = num//5
            elif num%3 == 0:
                num = num//3
            elif num%2 == 0:
                num = num//2
            else:
                return False

        return True

# Faster, better
class Solution:
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 1: return False
        while not (num % 2): num //= 2
        while not (num % 3): num //= 3
        while not (num % 5): num //= 5
        return num == 1
