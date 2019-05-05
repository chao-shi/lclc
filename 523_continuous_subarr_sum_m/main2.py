class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if k == 0:
            return any(nums[i] == nums[i-1] == 0 for i in range(1, len(nums)))

        accu_mod_map = {0: 0}
        accu_sum = 0
        for i in range(len(nums)):
            accu_sum = nums[i] + accu_sum
            if accu_sum % k in accu_mod_map:
                if i + 1 - accu_mod_map[accu_sum % k] >= 2:
                    return True
            else:
                accu_mod_map[accu_sum % k] = i + 1
        return False
    
# Careful case when k = 0
# Initialize accu_mod_map line 14, 0 and nums[0]

# Instead of keeping sliding window behind with two positions. We can check later. on line 16
    