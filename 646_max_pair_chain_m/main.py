class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        if not pairs:
            return 0
        pairs = sorted(pairs, key=lambda x:x[0])
        res = [pairs[0]]
        
        for i in range(1, len(pairs)):
            if pairs[i][0] > res[-1][1]:
                res.append(pairs[i])
            elif pairs[i][1] < res[-1][1]:
                res[-1] = pairs[i]
        return len(res)