class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        dest = stones[-1]
        stones = set(stones)
        def recur(x, step):
            if x == dest:
                return True
            for d in [1, 0, -1]:
                next_step = step + d
                next_x = x + next_step
                if next_step > 0 and next_x in stones and recur(next_x, next_step):
                    return True
            return False
        return recur(0, 0)