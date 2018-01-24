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
            elif i >= len(candidates):
                return
            else:
                nums.append(candidates[i])
                recur(i, nums, sumv + candidates[i])
                nums.pop()
                recur(i + 1, nums, sumv)
        recur(0, [], 0)
        return res

# 1. No state intersection
# 2. How to evaluate the complexity
# suppose c1, c2 ... cn are similar values
# target is much bigger than them
# we need K = target / c_avg elements
# We need to distribute K elements into n buckets
# (n, K) complexity
# Not sure if this is right ...