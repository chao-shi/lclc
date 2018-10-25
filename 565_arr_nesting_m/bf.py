class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_len = 0
        for i in range(len(nums)):
            used = set()
            p = i
            while p not in used:
                used.add(p)
                p = nums[p]
            max_len = max(max_len, len(used))
        return max_len
            