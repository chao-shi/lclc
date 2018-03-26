class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        def recur(nums, sum):
            if len(nums) == k and sum == n:
                res.append(nums[:])
            elif len(nums) < k:
                start = nums[-1] + 1 if nums else 1
                for i in range(start, 10):
                    recur(nums + [i], sum + i)
        
        recur([], 0)
        return res
    
# Complexity 10 ** k: exponential
# Only DFS, no DP