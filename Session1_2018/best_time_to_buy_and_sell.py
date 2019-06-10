class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        min_price = 99999999999999
        max_sell = 0
        for i in range(0, len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            else:
                if (prices[i] - min_price) > max_sell:
                    max_sell = prices[i] - min_price
        return max_sell
                
