class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        last = {}
        i = 0
        maxv = 0
        for j, ch in enumerate(s):
            if last.get(ch, -1) >= i:
                i = last[ch] + 1
            last[ch] = j
            maxv = max(maxv, j - i + 1)
        return maxv

# Left pointer no need to move one by one

# The key idea is not to use window {char:index}
# When i moves to the right, no need to pop from window map actively
# Instead
# use the last index map, and lazily compare with the left boundary of window