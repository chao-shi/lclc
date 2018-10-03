class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [()]
        for num in nums:
            for i in range(len(res)):
                seq = res[i]
                if not seq or seq[-1] <= num:
                    res.append(seq + (num,))
        return map(list, set(filter(lambda x:len(x) >= 2, res)))
        