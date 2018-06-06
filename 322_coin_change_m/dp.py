class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # amount + 1 to represent inf
        mt = [[amount + 1] * (len(coins) + 1) for i in range(amount + 1)]
        
        for j in range(len(coins) + 1):
            mt[0][j] = 0

        for i in xrange(1, amount + 1):
            for j in xrange(1, len(coins) + 1):
                mt[i][j] = mt[i][j-1]
                if i - coins[j-1] >= 0:
                    mt[i][j] = min(mt[i][j], mt[i-coins[j-1]][j] + 1)
        return -1 if mt[amount][len(coins)] == amount + 1 else mt[amount][len(coins)]

# DP does not pass OJ, but still faster than memory table recursion (Not much search space saver)