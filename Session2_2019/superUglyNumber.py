class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        uglydp = [1]
        p = len(primes)
        prime_idx = [0]*p
        prime_vals = [1]*p
        min_val = 1
        for i in range(1, n):
            for k in range(p):
                if prime_vals[k] == min_val:
                    prime_vals[k] = primes[k]*uglydp[prime_idx[k]]
                    prime_idx[k] += 1
                    # print(min_val, k, prime_idx, prime_vals, uglydp)
            min_val = min(prime_vals)
            uglydp.append(min_val)

        return uglydp[-1]
