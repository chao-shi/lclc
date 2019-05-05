class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        n = len(coins)
        mt = [[0] * (n + 1) for _ in range(amount + 1)]
        
        for i in range(n+1):
            mt[0][i] = 1
        
        for i in range(1, amount + 1):
            for j in range(1, n + 1):
                mt[i][j] = mt[i][j-1]
                remain = i - coins[j-1]
                if remain >= 0:
                    mt[i][j] += mt[remain][j]
        return mt[amount][n]