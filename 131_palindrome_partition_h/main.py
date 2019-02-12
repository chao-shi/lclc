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
        
        palin_map = palinMap(s)
        palins = [[[]]]
        for i, ch in enumerate(s):
            res = []
            for j in range(i + 1):
                if palin_map[j][i+1]:
                    res.extend(prefix + [s[j:i+1]] for prefix in palins[j])
            palins.append(res)
        return palins[-1]