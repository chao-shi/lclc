class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        cnt = collections.Counter(nums)
        j = 0
        for i in range(3):
            for k in range(cnt.get(i, 0)):
                nums[j] = i
                j += 1

# Line 10 counter get default value