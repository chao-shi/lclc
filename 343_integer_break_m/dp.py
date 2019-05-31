class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        res = [0, 0]
        for i in range(2, n+1):
            maxv = 0
            for left in range(1, i / 2 + 1):
                right = i - left
                maxv = max(maxv, max(left, res[left]) * max(right, res[right]))
            res.append(maxv)
        return res[-1]

print Solution().integerBreak(10)