class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        i = 0
        cnt = 0
        while i < len(A):
            j = i + 2
            while j < len(A) and A[j] - A[j-1] == A[j-1] - A[j-2]:
                j += 1

            # Longest arithmetic is A[i:j]
            # if j - i == 2 means no matching found.
            length = j - i
            # 1 + 2 + ... length - 2
            cnt += (length - 1) * (length - 2) / 2
            
            i = j - 1
            # Not NOT i = j
        return cnt

# Test case of [1,2,3,4, 6, 8]
# Careful line 20