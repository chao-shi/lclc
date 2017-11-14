class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        maxset = []
        nums = sorted(nums)
        for i in range(len(nums)):
            cands = [maxset[j] + [nums[i]] for j in range(len(maxset)) if nums[i] % nums[j] == 0] + [[nums[i]]]
            maxset.append(max(cands, key=lambda x:len(x)))
        
        if maxset:
            return max(maxset, key=lambda x:len(x))
        else:
            return []

# Brute force N^2
# Note line 16 because of case when max takes empty list as argument
# maxset[i] stores largest divisible set using element nums[i]

# We don't use maxset[i+1] to represent like usual because otherwise line 10 need if/else for maxset[0]