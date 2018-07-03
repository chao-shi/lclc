class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        cap = 0
        i = 0
        patch_cnt = 0
        while cap < n:
            if i < len(nums) and nums[i] <= cap + 1:
                cap += nums[i]
                i += 1
            else:
                patch_cnt += 1
                cap = cap * 2 + 1
        return patch_cnt