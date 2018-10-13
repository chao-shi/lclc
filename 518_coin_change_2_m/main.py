class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        mt = {}
        def recur(target, n):
            if target == 0:
                return 1
            elif target < 0 or n <= 0:
                return 0
            elif (target, n) in mt:
                return mt[(target, n)]
            else:
                ret = recur(target, n-1) + recur(target - coins[n-1], n)
                mt[(target, n)] = ret
                return ret
        
        return recur(amount, len(coins))
        