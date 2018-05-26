class Solution(object):
    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        def nexts(s):
            res = []
            for i in range(len(s) - 1):
                if s[i:i+2] == "++":
                    res.append(s[:i] + "--" + s[i+2:])
            return res
        
        mt = {}
        def recur(s):
            if s in mt:
                return mt[s]
            mt[s] = any(recur(next_state) == False for next_state in nexts(s))
            return mt[s]
        
        return recur(s)