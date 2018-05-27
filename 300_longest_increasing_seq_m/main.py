class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last = []
        for num in nums:
            idx = bisect.bisect_left(last, num)
            if idx == len(last):
                last.append(num)
            else:
                last[idx] = num
        return len(last)

# Initialize to be empty and bisect takes care
# NlogN