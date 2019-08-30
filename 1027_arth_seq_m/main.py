class Solution(object):
    def longestArithSeqLength(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        diff_map = collections.defaultdict(dict)
        max_len = 0
        for i in range(len(A) - 2, -1, -1):
            for j in range(len(A) - 1, i, -1):
                # Now first two elements is A[i], A[j]
                diff = A[j] - A[i]
                # we check if anything can start from j with delta
                # == diff
                # diff_map[j] is already fully populated when
                # j itself was in the outloop 8, when j was i
                cand_len = diff_map[j].get(diff, 1)
                diff_map[i][diff] = max(diff_map[i].get(diff, 1), cand_len + 1)
                max_len = max(max_len, cand_len + 1)
        return max_len