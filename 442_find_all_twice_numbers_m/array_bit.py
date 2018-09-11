class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        for i, num in enumerate(nums):
            real_num = num
            while real_num > n:
                real_num -= n
            
            nums[real_num - 1] += n
        
        res = []
        for i, num in enumerate(nums):
            if num > 2 * n:
                res.append(i + 1)
        return res

# Stupid question, not really O(N)