class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res = [1] * (rowIndex + 1)
        for j in range(1, rowIndex + 1):
            last = res[0]
            for i in range(1, j):
                last, res[i] = res[i],  res[i] + last
        return res
# line 9