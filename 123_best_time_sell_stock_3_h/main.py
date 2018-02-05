class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        A = [-prices[0]]
        B = [0]
        C = [-prices[0]]
        D = [0]
        for i in range(1, len(prices)):
            a = max(A[-1], -prices[i])
            b = max(B[-1], A[-1] + prices[i])
            c = max(C[-1], B[-1] - prices[i])
            d = max(D[-1], C[-1] + prices[i])
            A.append(a)
            B.append(b)
            C.append(c)
            D.append(d)
        return max(D)