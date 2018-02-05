class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return None
        m = [triangle[0][0]]
        for i in range(1, len(triangle)):
            mm = [min(m[j], m[j-1]) + triangle[i][j] for j in range(1, len(triangle[i]) - 1)]
            m = [m[0] + triangle[i][0]] + mm + [m[-1] + triangle[i][-1]]
        return min(m)