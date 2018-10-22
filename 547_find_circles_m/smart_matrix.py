import numpy as np
from numpy.linalg import matrix_power
class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        n = len(M)
        Mb = np.matrix(M, dtype='bool')
        Mn = matrix_power(Mb, n-1).tolist()

        # Same clique will have the same row.
        return len(set(map(tuple, Mn)))
                