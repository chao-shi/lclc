class Solution(object):
    def longestOnes(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        cnt_map = collections.defaultdict(int)
        max_win = 0
        i = 0
        for j in range(len(A)):
            cnt_map[A[j]] += 1
            while i <= j and cnt_map[0] > K:
                cnt_map[A[i]] -= 1
                i += 1
            win_size = j - i + 1
            max_win = max(max_win, win_size)
        return max_win