class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        for num in nums:
            res = [perm[:i] + [num] + perm[i:] for perm in res for i in range(len(perm) + 1)]
        return res