class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(s) < len(p):
            return []
        
        win = {}
        for i in range(len(p)):
            win[p[i]] = win.get(p[i], 0) - 1
            win[s[i]] = win.get(s[i], 0) + 1

        win = {ch:win[ch] for ch in win if win[ch] != 0}
        res = []
        
        # Don't forget corner case. First pair or last pair
        # Here we update win first then check, so last pair is considered in the loop
        # But not first pair
        if len(win) == 0:
            res.append(0)

        for i in range(len(p), len(s)):
            j = i - len(p)
                
            win[s[i]] = win.get(s[i], 0) + 1
            if win[s[i]] == 0:
                del win[s[i]]

            win[s[j]] = win.get(s[j], 0) - 1
            if win[s[j]] == 0:
                del win[s[j]]
                
            if len(win) == 0:
                res.append(j + 1)
        
        return res
    
# Careful about corner case
# 