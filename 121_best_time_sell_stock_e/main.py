class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        maxprofit = 0
        minprice = prices[0]
        for i in range(1, len(prices)):
            maxprofit = max(prices[i] - minprice, maxprofit)
            minprice = min(prices[i], minprice)
        return maxprofit