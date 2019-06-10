class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n == 1 or n == 2:
            return 0
        primes = [True]*n
        primes[0] = primes[1] = False

        for i, val in enumerate(primes):
            if val:
                for j in range(i*i, n, i):
                    primes[j] = False

        res = [i for i in primes if i]
        return len(res)
            
