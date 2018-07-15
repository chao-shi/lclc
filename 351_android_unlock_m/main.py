class Solution(object):
    def numberOfPatterns(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        def valid(seq, next):
            if next in seq:
                return False
            last = seq[-1]
            
            # horizontal or vertical
            if (abs(last - next) == 2 and max(last, next) % 3 == 0) or abs(last - next) == 6:
                cross = (last + next) / 2
                if cross not in seq:
                    return False
            
            # cover diagonal (loose case)
            if last + next == 10 and 5 not in seq:
                return False

            return True
            
            
        cnt = 0
        cands = [[i] for i in range(1, 10)]
        for length in range(1, n + 1):
            if m <= length <= n:
                cnt += len(cands)

            new_cands = []
            for cand in cands:
                for next in range(1, 10):
                    if valid(cand, next):
                        new_cands.append(cand + [next])
            cands = new_cands
        return cnt

# MLE, how to solve it

# A trick like mem_opt.py
# Or use backtracking, then memory only keep no more than 9 

# The number of permutation is huge. It will be a little slower for both methods