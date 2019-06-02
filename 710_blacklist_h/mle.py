class Solution(object):

    def __init__(self, N, blacklist):
        """
        :type N: int
        :type blacklist: List[int]
        """
        rmap = {}
        j = N - 1
        blacklist = set(blacklist)
        for i in range(N - len(blacklist)):
            if i in blacklist:
                while j >= N - len(blacklist) and j in blacklist:
                    j -= 1
                rmap[i] = j
        self.n, self.rmap = N - len(blacklist), rmap
        print self.rmap

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