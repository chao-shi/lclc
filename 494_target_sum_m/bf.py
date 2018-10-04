class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        self.cnt = 0
        def recur(signs):
            if len(signs) == len(nums) and len(signs) > 0:
                expr = []
                for i in range(len(nums)):
                    expr.extend([signs[i], str(nums[i])])
                expr = "".join(expr)
                if eval(expr) == S:
                    self.cnt += 1
        
            else:
                recur(signs + ["+"])
                recur(signs + ["-"])
                
        recur([])
        return self.cnt
                    
        
# TLE for [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], 1

print Solution().findTargetSumWays([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], 1)