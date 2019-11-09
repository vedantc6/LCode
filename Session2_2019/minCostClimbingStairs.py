class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n = len(cost)
        minCost = [0]*(n+1)

        for i in range(2, n+1):
            minCost[i] = min(minCost[i-1] + cost[i-1], minCost[i-2] + cost[i-2])

        return minCost[n]
