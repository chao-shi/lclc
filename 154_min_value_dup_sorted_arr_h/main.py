class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        li, hi = 0, len(nums) - 1
        while li <= hi:
            mid = (li + hi)/2
            if li == hi or nums[li] < nums[hi]:
                return nums[li]
            elif nums[li] > nums[mid]:
                hi = mid
            elif nums[mid] > nums[hi]:
                li = mid + 1
            else:
                # all equal and li != hi
                li += 1