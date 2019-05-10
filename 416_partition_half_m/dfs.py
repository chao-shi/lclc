class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hm = {}
        def dfs(i, target):
            if target == 0:
                return True
            elif target < 0 or i == 0:
                return False
            elif (i, target) in hm:
                return hm[(i, target)]
            v = dfs(i - 1, target - nums[i-1]) or dfs(i - 1, target)
            hm[(i, target)] = v
            return v
        
        total_sum = sum(nums)
        return dfs(len(nums), total_sum / 2) if total_sum % 2 == 0 else False