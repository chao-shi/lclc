class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        m = [0] * (target + 1)
        m[0] = 1
        for i in range(1, target + 1):
            for j in range(len(nums)):
                if i - nums[j] >= 0:
                    m[i] += m[i-nums[j]]
        return m[target]