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

        # assigned = [None] * len(nums) 
        # assigned[0] = 0

        nums = sorted(nums)
        
        def recur(i, length):
            # print i, assigned, length
            if i == len(nums):
                return True
            for j in range(4):
                if nums[i] + length[j] <= edge:
                    length[j] += nums[i]
                    # assigned[i] = j
                    if recur(i + 1, length):
                        return True
                    length[j] -= nums[i]
                    # assigned[i] = None
                elif length[j] < edge:
                    return False
            return False
        
        length = [nums[0], 0, 0, 0]
        return recur(1, length)

# print Solution().makesquare([211559,9514615,7412176,5656677,3816020,452925,7979371,5025276,8882605,944541,9889007,2344356,7252152,749758,2311818])

# To optimize on 2, I sort the nums and add another early termination condition on block 33.
# Still TLE