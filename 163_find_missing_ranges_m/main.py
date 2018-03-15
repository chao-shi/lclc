class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        nums = [lower - 1] + nums + [upper + 1]
        ranges = []

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1] + 1:
                ranges.append((nums[i-1] + 1, nums[i] - 1))
        
        return [str(r[0]) if r[0] == r[1] else str(r[0]) + "->" + str(r[1]) for r in ranges] 

# Line 9