import numpy as np
from numpy.linalg import matrix_power
class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        # Need to use boolean numpy to avoid overflow
        n = len(M)
        Mb = np.matrix(M, dtype='bool')
        # Convert back to list
        Mn = matrix_power(Mb, n-1).tolist()

        avail = set(range(0, n))
        clique_cnt = 0
        for i in range(0, n):
            if i in avail:
                clique_cnt += 1
                avail.remove(i)
                for j in range(i + 1, n):
                    if j in avail and Mn[i][j]:
                        avail.remove(j)
        return clique_cnt
                