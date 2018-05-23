class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        smaller = True
        
        for i in range(len(nums) - 1):
            # if smaller and nums[i] > nums[i+1] or not smaller and nums[i] < nums[i+1]:
            # Or a little trcik or XOR
            if smaller ^ (nums[i] <= nums[i+1]):  
                nums[i], nums[i+1] = nums[i+1], nums[i]
            smaller = not smaller
        