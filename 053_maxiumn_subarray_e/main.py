class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minacc = 0
        acc = 0
        maxv = None
        for num in nums:
            acc += num
            if maxv  == None or acc - minacc > maxv:
                maxv = acc - minacc
            minacc = min(minacc, acc)
        return maxv

# Handles empty array well enough