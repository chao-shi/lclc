class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        if not matrix:
            return None
        n, m = len(matrix), len(matrix[0])
        li, hi = matrix[0][0], matrix[-1][-1]
        while li <= hi:
            mid = (li + hi)/2
            cntl, cntle = 0, 0
            j1, j2 = m - 1, m - 1
            for i in range(n):
                while j1 >= 0 and matrix[i][j1] >= mid:
                    j1 -= 1
                while j2 >= 0 and matrix[i][j2] > mid:
                    j2 -= 1
                cntl += j1 + 1
                cntle += j2 + 1
            if cntl < k <= cntle:
                return mid
            elif k > cntle:
                li = mid + 1
            else:
                hi = mid - 1
        