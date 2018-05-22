class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        cnt = [0] * (n + 1)
        for c in citations:
            if c >= n:
                cnt[n] += 1
            else:
                cnt[c] += 1

        cnt_at_least = 0
        for h_index in range(n, -1, -1):
            cnt_at_least += cnt[h_index]
            if cnt_at_least >= h_index:
                return h_index                