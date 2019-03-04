class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        mt = [0] * (target + 1)
        mt[0] = 1
        for i in range(len(nums)):
            for v in range(0, target + 1):
                if v >= nums[i]:
                    mt[v] += mt[v-nums[i]]
            print mt

        return mt[target]