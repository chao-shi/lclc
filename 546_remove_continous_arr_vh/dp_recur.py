class Solution(object):
    def removeBoxes(self, boxes):
        """
        :type boxes: List[int]
        :rtype: int
        """
        mt = {}
        def recur(i, j, k):
            if (i, j, k) in mt:
                return mt[(i, j, k)]
            elif j == i:
                return 0
            maxv = (k + 1) ** 2 + recur(i+1, j, 0)
            for m in range(i+1, j):
                if boxes[m] == boxes[i]:
                    # Second term used k + 1, very tricky
                    maxv = max(maxv, recur(i+1, m, 0) + recur(m, j, k + 1))
            mt[(i, j, k)] = maxv
            return maxv
        return recur(0, len(boxes), 0)
    

