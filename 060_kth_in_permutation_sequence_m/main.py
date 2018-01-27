class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        k -= 1

        total = math.factorial(n)
        
        res = [0] * n
        cands = range(1, n+1)
        for i in range(n):
            bucket_size = total / (n - i)
            res[i] = cands.pop(k / bucket_size)
            k %= bucket_size
            total = bucket_size
        return "".join(map(str, res))
    
# Line 8 easy on 0 base
# Careful about division by zero
# good to iterate on total and bucket size