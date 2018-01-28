class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = 3
        start = [0] * 3
        for i, num in enumerate(nums):
            idx = i
            for k in range(n-1, num, -1):
                nums[start[k]], nums[idx] = nums[idx], nums[start[k]]
                idx = start[k]
                start[k] += 1

# More generaal case [0,4] example
# 0, 0, 1, 3, 3, 4, 4 is in place
# next element is 1

# swap 1 with first 4 and increment start of 4
# 0, 0, 1, 3, 3, 1, 4, 4

# swap 1 with first of 3
# 0, 0, 1, 1, 3, 3, 4, 4

# swap 1 with first of 2, no real swap happens, 
# BUT BUT start of 2 also increment by 1

# stop at 1
# finally we have 0, 0, 1, 1, 3, 3, 4, 4
