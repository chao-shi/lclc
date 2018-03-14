class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxvalue = None
        minprod, maxprod = 1, 1
        for num in nums:
            tmp = [maxprod * num, minprod * num, num]
            minprod, maxprod = min(tmp), max(tmp)
            maxvalue = max(maxvalue, maxprod)
        return maxvalue