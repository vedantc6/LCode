class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        cost.append(0)
        n = len(cost)
        minArray = [0]*n
        minArray[0] = minArray[1] = 0
        for i in range(2, n):
            minArray[i] = min(minArray[i-1] + cost[i-1], minArray[i-2] + cost[i-2])
        print(minArray)
        return minArray[n-1]
        
