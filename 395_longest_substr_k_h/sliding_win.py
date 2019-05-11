class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        max_len = 0
        for char_cnt in range(1, 27):
            i = 0
            cnt_map = collections.defaultdict(int)
            for j in range(len(s)):
                cnt_map[s[j]] += 1

                # Move left pointer
                while i <= j and len(cnt_map) > char_cnt:
                    cnt_map[s[i]] -= 1
                    if cnt_map[s[i]] == 0:
                        del cnt_map[s[i]]
                    i += 1

                if all(cnt_map[char] >= k for char in cnt_map):
                    max_len = max(max_len, j - i + 1)
        return max_len
