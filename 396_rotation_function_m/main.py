class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A_sum = sum(A)
        F = sum([i * num for i, num in enumerate(A)])
        maxv = F
        j = len(A) - 1
        for i in range(1, len(A)):
            F += A_sum - len(A) * A[j]
            maxv = max(maxv, F)
            j -= 1
        return maxv

# Math problem