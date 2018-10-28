class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt_map = collections.defaultdict(int)
        for num in nums:
            cnt_map[num] += 1
        
        max_len = 0
        for n in cnt_map:
            if n + 1 in cnt_map:
                max_len = max(max_len, cnt_map[n] + cnt_map[n+1])
        return max_len
            