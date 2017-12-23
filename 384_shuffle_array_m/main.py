# In shuffle, use the idea of index array

class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.nums
        

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        idx = range(len(self.nums))
        for i in range(len(idx)):
            rand = random.randint(i, len(idx) - 1)
            idx[i], idx[rand] = idx[rand], idx[i]
        return [self.nums[i] for i in idx]


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()