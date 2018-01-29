class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        pset = [[]]
        for num in nums:
            pset.extend([subset + [num] for subset in pset])
        return pset
        