class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        has_stock, no_stock = [-prices[0], -min(prices[:2])], [0, max(0, prices[1] - prices[0])]
        for i in range(2, len(prices)):
            sell = max(has_stock[-1] + prices[i], no_stock[-1])
            buy = max(has_stock[-1], no_stock[-2] - prices[i])
            has_stock.append(buy)
            no_stock.append(sell)
        return no_stock[-1]
        