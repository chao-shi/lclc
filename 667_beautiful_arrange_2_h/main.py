class Solution(object):
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        res = []
        for i in range(k/2):
            res.extend([i + 1, n - i])
        i = k / 2 + 1
        seq = range(i, i + n - len(res)) 
        res.extend(seq if k % 2 == 1 else seq[::-1])
        return res

# 1, 2, 3, 4, 5, 6    1: 1, 2, 3, 4, 5, 6
# 1, 6, 5, 4, 3, 2    2: (1, 6), 5, 4, 3, 2
# 1, 6, 2, 3, 4, 5    3: (1, 6), 2, 3, 4, 5
# 1, 6, 2, 5, 4, 3    4: (1, 6), (2, 5), 4, 3
# 1, 6, 2, 5, 3, 4.
# 
# Make sense to place n - 1 diff first, because only 1 pair.