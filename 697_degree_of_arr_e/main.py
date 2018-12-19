class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt_map = collections.defaultdict(int)
        for num in nums:
            cnt_map[num] += 1
        max_f = max(cnt_map.values())
        
        cnt_map = collections.defaultdict(int)
        first_idx = {}
        min_len = len(nums)
        for i, num in enumerate(nums):
            if num not in first_idx:
                first_idx[num] = i
            cnt_map[num] += 1
            if cnt_map[num] == max_f:
                min_len = min(min_len, i + 1 - first_idx[num])
        return min_len        