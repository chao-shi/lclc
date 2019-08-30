class Solution(object):
    def intervalIntersection(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        def findOverlap(intv1, intv2):
            if intv2[0] > intv1[1] or intv1[0] > intv2[1]:
                return None
            else:
                return [max(intv1[0], intv2[0]), min(intv1[1], intv2[1])]
        
        
        i, j = 0, 0
        res = []
        while i < len(A) and j < len(B):
            overlap = findOverlap(A[i], B[j])
            if overlap != None:
                res.append(overlap)
            if A[i][1] < B[j][1]:
                i += 1
            elif A[i][1] > B[j][1]:
                j += 1
            else:
                i, j = i + 1, j + 1
        return res
        