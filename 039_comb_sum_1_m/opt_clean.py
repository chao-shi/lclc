class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        def recur(i, nums, sumv):
            if sumv == target:
                res.append(nums[:])
            elif sumv > target:
                return
            else:
                for ii in range(i, len(candidates)):
                    nums.append(candidates[ii])
                    sumv += candidates[ii]
                    recur(ii, nums, sumv)
                    sumv -= candidates[ii]
                    nums.pop()
        recur(0, [], 0)
        return res