class Solution(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        self.cnt = 0
        self.mt = {}
        
        def recur(avail):
            if len(avail) == 0:
                return 1
            
            tp = tuple(avail)

            if tp in self.mt:
                return self.mt[tp]

            sum_v = 0
            i = N - len(avail)
            for cand in list(avail):
                if cand % (i+1) == 0 or (i+1) % cand == 0:
                    avail.remove(cand)
                    sum_v += recur(avail)
                    avail.add(cand)
            
            self.mt[tp] = sum_v
            return sum_v
 
        return recur(set(range(1, N+1)))