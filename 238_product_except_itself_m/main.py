class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = [1] * len(nums)
        for i in range(1, len(nums)):
            output[i] = output[i-1] * nums[i-1]
        
        prod = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= prod
            prod *= nums[i]
            
        return output