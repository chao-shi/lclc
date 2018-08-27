class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hm = {}
        def dfs(i, cur_sum, target):
            if i == len(nums):
                return False
            elif cur_sum == target:
                return True
            elif cur_sum > target:
                return False
            elif (i, cur_sum) in hm:
                return hm[(i, cur_sum)]
            v = dfs(i + 1, cur_sum + nums[i], target) or dfs(i + 1, cur_sum, target)
            hm[(i, cur_sum)] = v
            return v
        
        total_sum = sum(nums)
        return dfs(0, 0, total_sum / 2) if total_sum % 2 == 0 else False

# Line 13, don't forget