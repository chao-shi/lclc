class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        self.cnt = 0
        mt = {}

        def recur(i, sum):
            if i == len(nums):
                return 1 if sum == S else 0
            elif (i, sum) in mt:
                # Another signs with length i also add to sum
                # No more need to search below
                return mt[(i, sum)]
            else:
                c1 = recur(i + 1, sum + nums[i])
                c2 = recur(i + 1, sum - nums[i])
                mt[(i, sum)] = c1 + c2
                return c1 + c2
        return recur(0, 0)
                    
# How to prune nodes
        