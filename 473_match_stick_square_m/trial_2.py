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
            return False
        
        length = [nums[0], 0, 0, 0]
        return recur(1, length)

# print Solution().makesquare([211559,9514615,7412176,5656677,3816020,452925,7979371,5025276,8882605,944541,9889007,2344356,7252152,749758,2311818])

# Good thought, how to solve the symmetric issue by always setting first stick to edge 0
# 
# If you run this solution using the sample example.sample
# You will find when around i = 14, none of edges are filled with exact value.
# 
# Sample output:
# 10 [0, 3, 3, 2, 2, 3, 2, 1, 1, 1, None, None, None, None, None] [211559, 14852422, 17452068, 17379716]
# 11 [0, 3, 3, 2, 2, 3, 2, 1, 1, 1, 0, None, None, None, None] [10100566, 14852422, 17452068, 17379716]
# 12 [0, 3, 3, 2, 2, 3, 2, 1, 1, 1, 0, 0, None, None, None] [12444922, 14852422, 17452068, 17379716]
# 12 [0, 3, 3, 2, 2, 3, 2, 1, 1, 1, 0, 1, None, None, None] [10100566, 17196778, 17452068, 17379716]
# 13 [0, 3, 3, 2, 2, 3, 2, 1, 1, 1, 0, 1, 0, None, None] [17352718, 17196778, 17452068, 17379716]
# 14 [0, 3, 3, 2, 2, 3, 2, 1, 1, 1, 0, 1, 0, 0, None] [18102476, 17196778, 17452068, 17379716]
# 14 [0, 3, 3, 2, 2, 3, 2, 1, 1, 1, 0, 1, 0, 1, None] [17352718, 17946536, 17452068, 17379716]
# 
# So we shouldn't go this far in the beginning. when no edges are matched exact target length.