class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        target, rem = divmod(sum(nums), k)
        if rem or max(nums) > target: return False

        memo = [None] * (1 << len(nums))
        memo[-1] = True
        def search(used, todo):
            if memo[used] is None:
                targ = (todo - 1) % target + 1
                memo[used] = any(search(used | (1<<i), todo - num)
                                 for i, num in enumerate(nums)
                                 if (used >> i) & 1 == 0 and num <= targ)
            return memo[used]

        return search(0, target * k)

# This given solution is nothing special. It uses too much memory. Bad solution
# How to understand targ = (todo - 1) % target + 1
# Suppose target is 10, then every time we close with one set, we will land some where multiple of target
# If target is 10
# So when the todo is 40, then the next number we can be at most 10,
# if the todo is 39, then max is 9.