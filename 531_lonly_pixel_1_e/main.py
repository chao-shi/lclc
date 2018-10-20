class Solution(object):
    def findLonelyPixel(self, picture):
        """
        :type picture: List[List[str]]
        :rtype: int
        """
        m, n = len(picture), len(picture[0])
        row = [0] * m
        col = [0] * n
        for i in range(m):
            for j in range(n):
                if picture[i][j] == 'B':
                    row[i] += 1
                    col[j] += 1
        
        cnt = 0 
        for i in range(m):
            for j in range(n):
                if picture[i][j] == 'B' and row[i] == col[j] == 1:
                    cnt += 1
        return cnt