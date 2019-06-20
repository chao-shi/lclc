class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        profit = 0
        last_high = None
        i = 0

        # careful about ending, the way we code will get stuck at last index
        # while i < len(prices)
        while i < len(prices) - 1:
            j = i
            while j + 1 < len(prices) and prices[j+1] <= prices[j]:
                j += 1
            
            i = j
            while j + 1 < len(prices) and prices[j + 1] >= prices[j]:
                j += 1
                
            if j < len(prices) and i < len(prices):
                # Check if going up streak.
                # Checking down streak may cause issue, because we don't know how 
                # much it will go up later, may cause wrong decision.
                low, high = prices[i], prices[j]
                if last_high == None:
                    delta = high - low - fee
                else:
                    delta = max(high - last_high, high - low - fee)
                if delta >= 0:
                    last_high = high
                    profit += delta
            i = j
                
        return profit

# This still does not pass for some test cases. Not sure how to fix it
# Not easy to write a correct greedy version, DP is way easierx