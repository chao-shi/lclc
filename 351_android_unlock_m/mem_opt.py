class Solution(object):
    def numberOfPatterns(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        def valid(cand, next):
            last, seq = cand
            if 1 << next & seq > 0:
                return False
            
            # horizontal or vertical
            if (abs(last - next) == 2 and max(last, next) % 3 == 0) or abs(last - next) == 6:
                cross = (last + next) / 2
                if 1 << cross & seq == 0:
                    return False
            
            # cover diagonal (loose case)
            if last + next == 10 and 1 << 5 & seq == 0:
                return False

            return True
            
            
        cnt = 0
        cands = [(i, 1 << i) for i in range(1, 10)]
        for length in range(1, n + 1):
            if m <= length <= n:
                cnt += len(cands)

            new_cands = []
            for cand in cands:
                for next in range(1, 10):
                    if valid(cand, next):
                        new_cands.append((next, cand[1] | (1 << next)))
            cands = new_cands
        return cnt