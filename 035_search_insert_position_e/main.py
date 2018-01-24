class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
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
        
        return firstBadVersion(nums, lambda x : x >= target)
        