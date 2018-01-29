class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        m = [[] for i in range(k + 1)]
        m[0].append([])
        for i in range(1, n+1):
            mm = [[] for ii in range(k + 1)]
            mm[0].append([])
            for j in range(1, min(k, i) + 1):
                mm[j] = m[j] + [comb + [i] for comb in m[j-1]]
            m = mm
        return m[k]

# Not so good
