class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        ugn = [0]*n
        ugn[0] = 1
        twop, threep, fivep = 0, 0, 0
        two, three, five = 2, 3, 5

        for i in range(1, n):
            ugn[i] = min(two, three, five)
            if ugn[i] == two:
                twop += 1
                two = ugn[twop]*2
            if ugn[i] == three:
                threep += 1
                three = ugn[threep]*3
            if ugn[i] == five:
                fivep += 1
                five = ugn[fivep]*5
        return ugn[-1]

        
