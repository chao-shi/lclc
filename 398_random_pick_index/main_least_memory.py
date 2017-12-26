class Solution(object):

    def __init__(self, nums):
        """
        
        :type nums: List[int]
        :type numsSize: int
        """
        self.nums = nums
        

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        seed = 1
        for i, num in enumerate(self.nums):
            if num == target:
                if random.randint(1, seed) == 1:
                    idx = i
                seed += 1
        return idx
        

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)

# Reservior sampling
# O(1) memory for init and pick