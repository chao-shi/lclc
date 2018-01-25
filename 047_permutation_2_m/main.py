class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        for num in nums:
            newres = []
            for perm in res:
                if num in perm:
                    first = perm.index(num)
                else:
                    first = len(perm)
                newres.extend([perm[:i] + [num] + perm[i:] for i in range(first + 1)])
            res = newres
        return res

# 110ms 62%