class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums) < 2:
            return False
        
        if k == 0:
            return any(nums[i] == nums[i-1] == 0 for i in range(1, len(nums)))

        accu_mod_map = set([0, nums[0] % k])
        accu_sum = nums[0]
        for i in range(1, len(nums)):
            accu_sum = nums[i] + accu_sum
            if accu_sum % k in accu_mod_map:
                return True
            accu_mod_map.add(accu_sum % k)
        return False
    
# Careful case when k = 0
# Initialize accu_mod_map line 14, 0 and nums[0]
    