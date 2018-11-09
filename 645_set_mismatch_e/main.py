class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        set_sum = sum(set(nums))
        a = sum(nums) - set_sum
        b = n * (n + 1) / 2 - set_sum
        return [a, b]
    
# The only constant space algorithm uses XOR. Not worth it