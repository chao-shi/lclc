class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        def palinMap(s):
            n = len(s)
            m = [[False] * (n + 1) for i in range(n+1)]
            for i in range(n+1):
                m[i][i] = True
            for i in range(n):
                m[i][i+1] = True
        
            for diff in range(2, n + 1):
                for i in range(n - diff + 1):
                    j = i + diff
                    m[i][j] = (s[i] == s[j-1] and m[i+1][j-1])
            return m
        
        n = len(s)
        m = palinMap(s)
        minpar = [0] * (n+1)
        for i in range(1, n+1):
            minpar[i] = min(minpar[j] + 1 for j in range(i) if m[j][i])
        
        if n == 0:
            return 0
        return minpar[n] - 1

# Easier to write in Iterative as no pruning needed