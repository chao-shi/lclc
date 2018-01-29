class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        comb = [[]]
        for i in range(1, k+1):
            comb = [c + [j] for c in comb for j in range((c[-1] if c else 0) + 1, n + 1)]
        return comb

# Corrent but does not pass OJ