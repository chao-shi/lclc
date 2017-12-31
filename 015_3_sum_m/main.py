class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        i = 0
        ret = []
        while i < len(nums) - 2:
            j, k = i+1, len(nums)-1
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    ret.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j+1]:
                        j += 1
                    j += 1
                    while j < k and nums[k] == nums[k-1]:
                        k -= 1
                    k -= 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                else:
                    k -= 1
            while i < len(nums) - 2 and nums[i] == nums[i+1]:
                i += 1
            i += 1
        return ret

# Better, only do equal skip for case line 13