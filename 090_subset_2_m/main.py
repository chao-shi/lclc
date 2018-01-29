class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        cnt = collections.Counter(nums)
        es = cnt.keys()
        res = [[]]
        for e in es:
            res.extend([comb + [e] * i for comb in res for i in range(1, cnt.get(e) + 1)])
        return res