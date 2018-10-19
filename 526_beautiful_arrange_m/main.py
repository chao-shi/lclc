class Solution(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        self.cnt = 0
        
        def recur(avail):
            if len(avail) == 0:
                self.cnt += 1
                return
            i = N - len(avail)
            cands = list(avail)
            for cand in cands:
                if cand % (i+1) == 0 or (i+1) % cand == 0:
                    avail.remove(cand)
                    recur(avail)
                    avail.add(cand)
        
        recur(set(range(1, N+1)))
        return self.cnt

# This is not fast enough