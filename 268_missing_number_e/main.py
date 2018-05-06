class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        r = 0
        for num in nums:
            r ^= num
        for i in range(len(nums)+1):
            r ^= i
        return r