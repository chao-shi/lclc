class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None

        li, hi = 0, len(nums) - 1
        while li < hi:
            mid = (li + hi) / 2
            if nums[mid] < nums[mid + 1]:
                # must be at least one peak on right
                li = mid + 1
            else:
                hi = mid
        return li