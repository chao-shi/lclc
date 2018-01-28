class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        
        m, n = len(matrix), len(matrix[0])
        # search vertically and find first > target, ignoring submatrix on the bottom starting from first
        lb, hb = 0, m - 1
        while lb <= hb:
            mid = (lb+hb)/2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] > target:
                hb = mid - 1
            else:
                lb = mid + 1
        
        if lb == 0:
            return False

        # search vertically and find first >= target, ignoring submatrix on the left ending before first
        row = lb - 1
        lb, hb = 0, n - 1
        while lb <= hb:
            mid = (lb+hb)/2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                hb = mid - 1
            else:
                lb = mid + 1
        return False

# Search strategy.
# Vertically search first >
# Horizontally, search first >=
