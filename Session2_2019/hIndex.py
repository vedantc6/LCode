class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        counts = [0 for i in range(n+1)]

        for c in citations:
            counts[min(c, n)] += 1

        k = n

        sum1 = 0

        for k in range(n, -1, -1):
            sum1 += counts[k]
            if k <= sum1:
                return k
