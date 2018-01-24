class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        li, hi = 0, len(nums) - 1
        while li <= hi:
            mid = (li + hi) / 2
            if nums[mid] == target:
                return mid
            elif nums[li] <= target < nums[mid] or nums[mid] < nums[li] <= target or target < nums[mid] < nums[li]: 
                hi = mid - 1
            else:
                li = mid + 1
        return -1

# Better than four case way