class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxlen = 0
        nums = set(nums)
        while nums:
            e = nums.pop()
            i = e - 1
            while i in nums:
                nums.remove(i)
                i -= 1
            j = e + 1
            while j in nums:
                nums.remove(j)
                j += 1
            maxlen = max(maxlen, j - i - 1)
        return maxlen