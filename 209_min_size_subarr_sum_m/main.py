class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        j = 0
        accj = 0
        acci = 0
        minwin = len(nums)
        for i, num in enumerate(nums):
            acci += nums[i]
            while acci - accj >= s:
                accj += nums[j]
                j += 1
            # sum(nums[j-1:i+1]) >= s
            if j > 0:
                minwin = min(minwin, i - j + 2)
        return minwin if j > 0 else 0

# Trick to assign minwin to be len(nums)
# line 18
        