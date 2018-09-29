class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_win = 0
        for i, num in enumerate(nums):
            if num == 0:
                i1, i2 = i - 1, i + 1
                while i1 >= 0 and nums[i1] == 1:
                    i1 -= 1
                while i2 < len(nums) and nums[i2] == 1:
                    i2 += 1
                max_win = max(max_win, i2 - i1 - 1)
                
        if max_win == 0 and nums:
            return len(nums)
        return max_win
                
# Test case [1, 1, ....]
# Does not work for stream case