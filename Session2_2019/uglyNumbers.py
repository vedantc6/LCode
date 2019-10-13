class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        def ugl(a, b):
            while a % b == 0:
                a = a//b
            return a

        if num < 1:
            return 0
        num = ugl(num, 2)
        num = ugl(num, 3)
        num = ugl(num, 5)
        return 1 if num == 1 else 0

# Faster
if num <= 0:
            return False
        for x in [2, 3, 5]:
            while num % x == 0:
                num = num / x
        return num == 1
