class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        temp = self.myPow(x, int(n/2))
        if n % 2 == 0:
            return temp*temp
        else:
            if n > 0:
                return temp*temp*x
            else:
                return temp*temp*(1/x)

        
