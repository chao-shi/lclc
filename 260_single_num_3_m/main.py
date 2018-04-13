class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor=0
        n=len(nums)
        for i in range(n):
            xor^=nums[i]
        
        # 110100 -> 000100
        # pick any bit also work
        bit=xor ^ (xor & (xor-1))
        
        # two groups now
        num1, num2 = 0,0
        for i in range(n):
            if nums[i] & bit > 0:
                num1^=nums[i]
            else:
                num2^=nums[i]
        return [num1, num2]
        
                