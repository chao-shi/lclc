class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Example 1, 2, 3, 4, 5
        # answer is max(P(1, 2, 3, 4), P(2, 3) + cost(5)
        # No good relationship between two subproblems, have to solve independently
        
        def rob_linear(li, hi):
            if hi - li < 1:
                return 0
            a, b = nums[li], 0
            for i in range(li + 1, hi):
                a, b = max(a, b + nums[i]), a
            return a
        
        if not nums:
            return 0
        return max(rob_linear(0, len(nums) - 1), rob_linear(1, len(nums)))

# No tricks, two sub problems

# This is wrong. I thought the problem is divided into 
# 1: Don't rob house[0]
# 2: Don't rob house[-1]

# This is wrong for case where len = 1, so the optimal solution does not always fall into either