class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        # View of linear combination of column vector of A
        m, n, k = len(A), len(B), len(B[0])
        res = [[0] * k for i in range(m)]

        A_col_cache = {}
        for j in range(k):
            for i in range(n):
                if B[i][j] == 0:
                    continue
                # Here we look at A column vector A[:][i]
                if i not in A_col_cache:
                    A_col_cache[i] = filter(lambda ii: A[ii][i] != 0, range(m))
                for ii in A_col_cache[i]:
                    res[ii][j] += A[ii][i] * B[i][j]
        return res
    
# Line 12 A_col_cache[i] stores which ii such that A[ii][i] != 0
# This approach lazy load A. May not need to read A at all in case of B all zero
