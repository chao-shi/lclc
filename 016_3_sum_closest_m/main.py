class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        closest = sys.maxint
        i = 0
        while i < len(nums) - 2:
            j, k = i + 1, len(nums) - 1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if abs(sum - target) < abs(closest-target):
                    # maxint + num will be long type
                    closest = sum
                if sum == target:
                    return target
                elif sum < target:
                    j += 1
                else:
                    k -= 1
            
            i += 1
        return closest