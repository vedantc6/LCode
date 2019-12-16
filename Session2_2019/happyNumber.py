class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def next_n(n):
            total = 0
            while n > 0:
                n, digit = divmod(n, 10)
                total += digit**2
            return total

        cycle = set()

        while n != 1 and n not in cycle:
            cycle.add(n)
            n = next_n(n)

        return n == 1
        
