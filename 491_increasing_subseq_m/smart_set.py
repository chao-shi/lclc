class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = {()}
        for num in nums:
            extend = set()
            for seq in res:
                if not seq or seq[-1] <= num:
                    extend.add(seq + (num,))
            res |= extend
        return map(list, set(filter(lambda x:len(x) >= 2, res)))
        
# Line 13 |=
# Initialize empty set has to be set(), not {}