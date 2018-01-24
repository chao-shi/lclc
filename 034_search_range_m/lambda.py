class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def firstBadVersion(nums, isBad):
            li, hi = 0, len(nums) - 1
            while li <= hi:
                mid = (li + hi)/2
                if isBad(nums[mid]):
                    hi = mid - 1
                else:
                    li = mid + 1
            return li
        
        hi = firstBadVersion(nums, lambda x : x > target)
        li = firstBadVersion(nums, lambda x : x >= target)
        if li == hi:
            return [-1, -1]
        return [li, hi - 1]
