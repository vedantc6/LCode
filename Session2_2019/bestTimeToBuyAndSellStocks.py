class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        minval = 9999999
        maxval = 0
        
        for i in range(len(prices)):
            if prices[i] < minval:
                minval = prices[i]
            elif prices[i] - minval > maxval:
                maxval = prices[i] - minval
                
        return maxval