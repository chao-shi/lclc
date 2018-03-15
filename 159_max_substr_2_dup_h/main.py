class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxv = 0
        j = 0
        last_map = {}
        for i, ch in enumerate(s):
            last_map[ch] = i
            if len(last_map) > 2:
                # rm_ch = last_map.items().sort(key=lambda x:x[1])[0]
                # rm_ch = min(last_map.keys(), key=last_map.get)
                rm_ch = min(last_map, key=last_map.get)
                j = last_map[rm_ch] + 1
                del last_map[rm_ch]
            maxv = max(maxv, i - j + 1)
        return maxv
            
# Line 13-15, how to do it better and better
# https://stackoverflow.com/questions/3282823/get-the-key-corresponding-to-the-minimum-value-within-a-dictionary