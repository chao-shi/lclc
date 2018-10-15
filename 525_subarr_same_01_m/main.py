class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        delta = 0
        delta_map = {0:0}
        ans = 0
        for i, num in enumerate(nums):
            delta += 1 if num == 0 else -1
            
            if delta in delta_map:
                ans = max(ans, i + 1 - delta_map[delta]) 
            else:
                delta_map[delta] = i + 1
        return ans