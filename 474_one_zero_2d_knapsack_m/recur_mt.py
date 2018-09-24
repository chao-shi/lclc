class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        cands = [(s.count("0"), s.count("1")) for s in strs]
        cands = [c for c in cands if c[0] <= m and c[1] <= n]
        mt = {}

        def recur(i, j, k):
            if k == 0:
                return 0
            elif (i, j, k) in mt:
                return mt[(i, j, k)]
            else:
                c0, c1 = cands[k-1]
                max_cnt = recur(i, j, k-1)
                if c0 <= i and c1 <= j:
                    max_cnt = max(max_cnt, recur(i-c0, j-c1, k-1) + 1)
                mt[(i, j, k)] = max_cnt
                return max_cnt

        return recur(m, n, len(cands))