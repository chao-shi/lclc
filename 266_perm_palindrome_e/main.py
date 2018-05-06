class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ch_map = {}
        cnt = 0
        for ch in s:
            ch_map[ch] = -ch_map.get(ch, -1)
            cnt += ch_map[ch]
        return cnt <= 1

# Use 1, -1 to represent T/F, easier to add/minus