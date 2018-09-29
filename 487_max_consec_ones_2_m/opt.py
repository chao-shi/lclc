class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_win = 0
        # win_left init to be -1 for non-existing first 0
        win_left, win_right = -1, 0
        for i, num in enumerate(nums):
            if num == 1:
                win_right += 1
            else:
                # Nicely fit all cases
                win_left = win_right
                win_right = 0
            max_win = max(max_win, win_right + win_left + 1)
        return max_win