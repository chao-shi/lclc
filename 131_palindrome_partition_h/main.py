class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
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
        hm = {}
        def recur(i):
            if i in hm:
                return hm[i]
            elif i == n:
                return [[]]
            res = []
            for j in range(i+1, n+1):
                if m[i][j]:
                    res.extend([s[i:j]] + ext for ext in recur(j))
            hm[i] = res
            return res
        
        if n == 0:
            return []
        return recur(0)
        
# Usually combination problem need block 36. Empty case need to return set of "phai" to make the derivation moves on