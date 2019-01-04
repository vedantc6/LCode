class Solution:
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1:
            return 0
        ugly = [0]*n
        ugly[0] = 1
        i2 = i3 = i5 = 0
        nm_2, nm_3, nm_5 = 2, 3, 5
        for i in range(1, n):
            ugly[i] = min(nm_2, nm_3, nm_5)
            if ugly[i] == nm_2:
                i2 += 1
                nm_2 = ugly[i2]*2
            if ugly[i] == nm_3:
                i3 += 1
                nm_3 = ugly[i3]*3
            if ugly[i] == nm_5:
                i5 += 1
                nm_5 = ugly[i5]*5

        return ugly[-1]
