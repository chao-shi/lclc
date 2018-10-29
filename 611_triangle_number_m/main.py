class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        # (i, j, k)
        cnt = 0
        for i in range(len(nums) - 2):
            k = i + 2
            for j in range(i + 1, len(nums) - 1):
                while k <= j or k < len(nums) and nums[k] < nums[i] + nums[j]:
                    k += 1
                cnt += (k - j - 1)
        return cnt
                
# Line 12 k <= j condition, otherwise k may becomes smaller than j if nums[i] is zero