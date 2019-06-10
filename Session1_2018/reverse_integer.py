class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = -1 if x < 0 else 1
        temp_str = str(abs(x))
        if len(temp_str) <= 1:
            return sign*int(temp_str)
        temp_str = temp_str[::-1]
        while(temp_str[0] == '0'):
            temp_str = temp_str[1:]
        res = int(temp_str)
        if (sign*res >= 2147483647 or sign*res <= -2147483648):
            return 0

        return sign*res

        
