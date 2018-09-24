class Solution(object):
    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # [] is not covered, the below will return true instead
        if not nums:
            return False

        peri = sum(nums)
        if peri % 4 != 0:
            return False
        edge = peri / 4
        
        def recur(i, length):
            if i == len(nums):
                return True
            for j in range(4):
                if nums[i] + length[j] <= edge:
                    length[j] += nums[i]
                    if recur(i + 1, length):
                        return True
                    length[j] -= nums[i]
            return False
        
        return recur(0, [0] * 4)

# TLE, idea is to assign each num an edge (0, 1, 2, 3)
# when call recur(i)
# Before i may looks like 0, 2, 1, 3, .... ? ....
# 