class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(sorted(nums)[::2])

# Solution 3 given by LC is stupid. Why don't just use count sort if you know the range is limited