class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        j = 0
        max_win = None
        win = 0
        for i in range(len(nums)):
            win += nums[i]
            if i - j + 1 > k:
                win -= nums[j]
                j += 1
            if i - j + 1 == k:
                max_win = win if max_win == None else max(max_win, win)
        return float(max_win) / float(k)