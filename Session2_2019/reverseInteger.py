class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        minInt = pow(-2, 31)
        maxInt = pow(2, 31) - 1
        if x < 0:
            sign = -1
        x = abs(x)
        reverse = 0
        while x > 0:
            reverse = reverse*10 + x % 10
            x = x // 10

        if reverse < minInt or reverse > maxInt:
            return 0
        return reverse*sign
            
