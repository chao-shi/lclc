class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        # Don't forget this k == 0
        if not prices or k == 0:
            return 0
        
        # Quick solution for OJ
        if k > len(prices)/2:
            return self.quicksolve(prices)
        
        states = [0] * (k * 2)
        for i in range(0, len(states), 2):
            states[i] = -prices[0]
        
        for i in range(1, len(prices)):
            newstates = [0] * (k * 2)
            for j in range(len(newstates)):
                if j == 0:
                    newstates[j] = max(states[j], -prices[i])
                elif j % 2 == 1:
                    # Sell here
                    newstates[j] = max(states[j], states[j-1] + prices[i])
                else:
                    # Buy here
                    newstates[j] = max(states[j], states[j-1] - prices[i])
            states = newstates
        return states[-1]
    
    def quicksolve(self, prices):
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        return profit

# states store after passing through prices[:i], what the best you can get
# - means buy, + means sell

# states     new states             value
# -              -                  min(state[0], -prices[i])
# -+             -+                 min(state[1], state[0] + prices[i])
# -+-            -+-                min(state[2], state[1] - prices[i])
# -+-+           -+-+               min(state[3], state[2] + prices[i])

# To tell the story another way
# A(n, k) up to stock A[:n] max money made with stock in hand, most kth buying happend
# B(n, k) up to stock A[:n] max money made with no stock in hand, most kth selling happend

# A(n, k) = max(A(n-1, k), B(n-1, k-1) - prices[n-1])  # Buy or not
# B(n, k) = max(B(n-1, k), A(n-1, k-1) + prices[n-1])  # Sell or not

# Base case will be n = 1
# case 1 cannot be derived well from case 0. A(0, k) assign to zero is wrong. 
# (With no stock prices, it is impossible to with some in hand) 