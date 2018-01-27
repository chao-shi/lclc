class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_jump = 0
        for i, num in enumerate(nums):
            if i > max_jump:
                return False
            elif max_jump >= len(nums) - 1:
                return True
            max_jump = max(max_jump, num + i)
        # always return before last case is i = len - 1, always covered by line 9 or line 11