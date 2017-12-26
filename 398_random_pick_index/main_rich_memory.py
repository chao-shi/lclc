class Solution(object):

    def __init__(self, nums):
        """
        
        :type nums: List[int]
        :type numsSize: int
        """
        self.index = {}
        for i, num in enumerate(nums):
            if num not in self.index:
                self.index[num] = []
            self.index[num].append(i)
        

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        idx = self.index[target]
        return idx[random.randint(1, len(idx)) - 1]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)

# O(N) memory for init, O(1) memory for pick

# Does not pass OJ