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
        return max(rob_linear(0, len(nums) - 1), rob_linear(1, len(nums) - 2) + nums[-1])

# No tricks, two sub problems