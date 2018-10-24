class Solution(object):
    def splitLoopedString(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strs = map(lambda x : max(x, x[::-1]), strs)
        max_ans = "".join(strs)

        for i in range(len(strs)):
            # We will attempt to split i
            mid_str = "".join(strs[i+1:] + strs[:i])
            for s in [strs[i], strs[i][::-1]]:
                for k in range(1, len(s) + 1):
                    cand = s[len(s) - k:] + mid_str + s[:len(s) - k]
                    max_ans = max(max_ans, cand)
                    
        return max_ans
                    
                
# just brute force, pretty fast, N^2 if the string length can be considered as constant