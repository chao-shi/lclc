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
        idx = [i for i, num in enumerate(self.nums) if num == target]
        return idx[random.randint(1, len(idx)) - 1]
        

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)

# To improve pick function, how to not store the indexes

# O(1) memory for init, O(N) for pick