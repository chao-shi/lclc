class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # the "step"th step explore to the new area of [a, b]
        a, b = 0, 0
        step = 0
        while True:
            if len(nums) - 1 <= b:
                return step
            a, b = b + 1, max([i + nums[i] for i in range(a, b+1)])
            step += 1
            
            # Todo how to always safely break, if [a, b] makes no progress forward
