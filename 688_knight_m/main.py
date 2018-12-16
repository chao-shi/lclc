class Solution(object):
    def knightProbability(self, N, K, r, c):
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """
        mt = {}
        
        def inside(i, j):
            return 0 <= i < N and 0 <= j < N

        def recur(i, j, remain):
            if not inside(i, j):
                return 0
            elif remain == 0:
                return 1
            elif (i, j, remain) in mt:
                return mt[(i, j, remain)]
            else:
                poss = 0
                for v in [(1, 2), (2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1), (-1, 2), (-2, 1)]:
                    poss += recur(i + v[0], j + v[1], remain - 1)
                mt[(i, j, remain)] = float(poss) / 8.0
                return float(poss) / 8.0
        
        return recur(r, c, K)