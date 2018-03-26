class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        last_idx = {}
        for i, num in enumerate(nums):
            if num in last_idx and i - last_idx[num] <= k:
                return True
            last_idx[num] = i
        return False