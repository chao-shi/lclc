class Solution(object):
    def magicalString(self, n):
        """
        :type n: int
        :rtype: int
        """
        # generate n
        # B is the current count representation of A
        # Careful about starting point
        A, B = [1, 2, 2], [1, 2]
        
        while len(A) < n:
            j = len(B)
            B.append(A[j])
            A.extend([3 - A[-1]]* A[j])
        return A[:n].count(1)
                
# There is also a magic string starting with 2. But not what the question looking for