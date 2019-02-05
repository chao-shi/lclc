class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates = sorted(candidates, reverse=True)
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

# 1. This is not utilizing the state crossing
# 2. How to evaluate the complexity
# suppose c1, c2 ... cn are similar values
# target is much bigger than them
# we need K = target / c_avg elements
# We need to distribute K elements into n buckets
# (n, K) complexity
# Not sure if this is right ...


# This is memeory cheap. For this problem it is not necessary longer in computation
# 1. It waste time in calculating the same state again and again
# 2. The calculate once and store approach also needs to copy the list around a lot. 
# So in OJ this is actually faster

# For Y/N or counting problem, this solution is not acceptable, because the issue 2 count
# and store does not have any more. 