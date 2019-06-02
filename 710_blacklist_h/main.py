class Solution(object):

    def __init__(self, N, blacklist):
        """
        :type N: int
        :type blacklist: List[int]
        """
        rmap = {}
        j = N - 1
        blacklist = set(blacklist)
        for blk in blacklist:
            if blk < N - len(blacklist):
                while j >= N - len(blacklist) and j in blacklist:
                    j -= 1
                rmap[blk] = j
                j -= 1
        self.n, self.rmap = N - len(blacklist), rmap

    def pick(self):
        """
        :rtype: int
        """
        idx = random.randint(0, self.n-1)
        return self.rmap.get(idx, idx)
        
# This initial set up is good when blacklist is very long.
# Reversely if black list is shorter. We can optmize by going backwards


# Your Solution object will be instantiated and called as such:
# obj = Solution(N, blacklist)
# param_1 = obj.pick()