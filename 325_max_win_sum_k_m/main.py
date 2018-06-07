class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sum = 0
        sum_map = {0: 0}
        max_win = 0
        for i, num in enumerate(nums):
            sum += num
            if sum - k in sum_map:
                max_win = max(max_win, i + 1 - sum_map[sum - k])
            sum_map.setdefault(sum, i+1)
        return max_win 
            
            