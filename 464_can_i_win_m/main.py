class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        mtable = {}
        n = maxChoosableInteger
        def recur(mask, remain):
            if (mask, remain) in mtable:
                return mtable[(mask, remain)]
            elif remain <= 0:
                return False
            for i in range(n):
                if mask & (1 << i) > 0:
                    new_mask = mask & ~(1 << i)
                    if not recur(new_mask, remain - i - 1):
                        mtable[(mask, remain)] = True
                        return True
            # Also cover case that no available next step
            mtable[(mask, remain)] = False
            return False
        
        if desiredTotal == 0:
            return True
        elif desiredTotal > (1 + n) * n / 2:
            return False
        return recur((1 << n) - 1, desiredTotal)
                    

# Corner case
# 1. Face with 0 at first
# 2. No one can win
# 1 can be avoided by structuring in different way, I.E. Try to see if i + 1 >= remain
# 2 cannot be avoided
# All children T: We are F
# If any of them are F, we don't know if we are T or F. This is the dilema.
# So we need precheck at line 27 