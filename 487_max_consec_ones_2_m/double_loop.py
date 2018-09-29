class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        max_win = 0
        while i < len(nums):
            if nums[i] == 1:
                i1 = i + 1
                while i1 < len(nums) and nums[i1] == 1:
                    i1 += 1
                max_win = max(max_win, i1 - i + (1 if i > 0 else 0))
                
                if i1 == len(nums) - 1 or (i1 < len(nums) - 1 and nums[i1+1] == 1):
                    i2 = i1 + 1
                    while i2 < len(nums) and nums[i2] == 1:
                        i2 += 1
                    max_win = max(max_win, i2 - i)
                
                i = i1 + 1
                # NOT i = i2
            else:
                i += 1

        if max_win == 0 and nums:
            return 1
        return max_win
        
# Test case [0]