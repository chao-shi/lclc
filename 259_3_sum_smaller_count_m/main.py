class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        cnt = 0
        i = 0
        
        while i < len(nums) - 2:
            j, k = i + 1, len(nums) - 1
            while j < k:
                while j < k and nums[i] + nums[j] + nums[k] >= target:
                    k -= 1
                cnt += k - j
                j += 1
            i += 1
        return cnt

# The problem did not ask to list all combos
# To list all, this problem is N^3
# Worst case target is infinite, needs to enumerate all combinations

# And it is asking unique indexes combos
# unique value combo cannot do O(n^2)