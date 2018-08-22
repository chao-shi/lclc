class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        dest = stones[-1]
        stones = set(stones)
        mt = {}
        def recur(x, step):
            if (x, step) in mt:
                return mt[(x, step)]
            if x == dest:
                return True
            
            res = False
            for d in [1, 0, -1]:
                next_step = step + d
                next_x = x + next_step
                if next_step > 0 and next_x in stones and recur(next_x, next_step):
                    res = True
                    break
            mt[(x, step)] = res
            return res
        return recur(0, 0)

# Struggle too much time. No tricks on the K-1, K, K+1 part. Need memory table
# 
# Things could happen like
# 5, 7, 8 or 6, 7, 8
# End up calling (8, 1) twice.
# 
# Complexity N^2


# Lesson leared:
# It is an DFS problem. 
# A repetitive pattern not so obvious.
# I figure out the repetitive pattern by looking back at the for loop solution.
