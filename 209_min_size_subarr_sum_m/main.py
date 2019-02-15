class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        win_sum = 0
        j = 0
        min_win = len(nums) + 1
        for i in range(len(nums)):
            win_sum += nums[i]
            if win_sum >= s:
                # all positive very important
                # This allows us to greedily stop moving j
                # once win_sum is below 2
                while win_sum >= s:
                    win_sum -= nums[j]
                    j += 1
                min_win = min(min_win, i - j + 2)
        
        return min_win if min_win <= len(nums) else 0

# Line 13 is important, two pointer sliding window always follow this pattern.
# If current window ending at i satisfy, try moving j
# If current window ending at i not satisfy, don't move j