class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res = [0] * (rowIndex + 1)
        res[0] = 1
        for i in range(rowIndex):
            res[i + 1] = 1
            for j in range(i, 0, -1):
                res[j] = res[j] + res[j-1]
        return res