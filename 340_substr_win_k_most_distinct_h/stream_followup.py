class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        max_win = 0
        last_idx = {}
        j = 0
        for i, ch in enumerate(s):
            last_idx[ch] = i
            if len(last_idx) > k:
                ch_rm, j = sorted(last_idx.items(), key=lambda tp: tp[1])[0]
                del last_idx[ch_rm]
                j += 1
            max_win = max(max_win, i - j + 1)
        return max_win
        
# For streaming, no need to iterate on j any more

# How to optmize on line 14, now we are sorting to get min
# What we need is a map which can get the key with the smallest value

# In Java we can do a HashMap<K, V> and TreeSet<Tuple<K, V>> TreeSet sorted by V first then K