class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        win_cnt = {}
        max_win = 0
        j = 0
        for i, ch in enumerate(s):
            win_cnt[ch] = win_cnt.get(ch, 0) + 1
            while len(win_cnt) > k:
                win_cnt[s[j]] -= 1
                if win_cnt[s[j]] == 0:
                    del win_cnt[s[j]]
                j += 1
            max_win = max(max_win, i - j + 1)
        return max_win