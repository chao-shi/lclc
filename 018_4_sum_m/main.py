class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        i = 0
        ret = []
        while i < len(nums) - 3:
            sum3 = self.threeSum(nums[i+1:], target - nums[i])
            ret.extend([[nums[i]] + tp for tp in sum3])
            while i < len(nums) - 3 and nums[i] == nums[i+1]:
                i += 1
            i += 1
        return ret
        
        
    def threeSum(self, nums, target):
        i = 0
        ret = []
        while i < len(nums) - 2:
            j, k = i+1, len(nums)-1
            while j < k:
                if nums[i] + nums[j] + nums[k] == target:
                    ret.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j+1]:
                        j += 1
                    j += 1
                    while j < k and nums[k] == nums[k-1]:
                        k -= 1
                    k -= 1
                elif nums[i] + nums[j] + nums[k] < target:
                    j += 1
                else:
                    k -= 1
            while i < len(nums) - 2 and nums[i] == nums[i+1]:
                i += 1
            i += 1
        return ret