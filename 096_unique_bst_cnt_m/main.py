class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        m = [1]
        for i in range(1, n+1):
            m.append(sum(m[k] * m[i-1-k] for k in range(i)))
        return m[-1]