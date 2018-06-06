class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # amount + 1 to represent inf
        row = [0] + [amount + 1] * amount

        for j in range(1, len(coins) + 1):
            new_row = row[:]
            for i in range(1, amount + 1):
                if i - coins[j-1] >= 0:
                    new_row[i] = min(new_row[i], new_row[i-coins[j-1]] + 1)
            row = new_row
        return -1 if row[-1] == amount + 1 else row[-1]

# Optimize storage usage