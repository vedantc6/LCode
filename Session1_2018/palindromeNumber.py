class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if x < 10:
            return True
        temp = x
        rem = 0
        while temp > 0:
            rem = rem*10 + temp % 10
            temp = temp//10

        if rem == x:
            return True
        else:
            return False
