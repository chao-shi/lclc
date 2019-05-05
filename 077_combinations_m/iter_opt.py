class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        # def enough(c, j):
            # return n - j + 1 >= k - len(c)
        comb = [[]]
        for i in range(1, k+1):
            comb = [c + [j] for c in comb for j in range((c[-1] if c else 0) + 1, n + 1) if j <= n - k + len(c) + 1]
        return comb

# ascending with checking. The key idea to fast things is the early pruning on line 12