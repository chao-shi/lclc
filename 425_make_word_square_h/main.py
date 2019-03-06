class Solution(object):
    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """
        # word length very small, trie doesn't help much
        
        # This is how large the square can go
        n = max(map(len, words))
        prefix_m = {}
        
        # "" is valid prefix to handle first line case
        for w in words:
            for i in range(len(w) + 1):
                prefix_m.setdefault(w[:i], set()).add(w)
                
        def recur(i, lines, sol):    
            # print i, lines[:i]
            # if i == n:
            if i > 0 and i == len(lines[0]):
                sol.append(list(lines[:i]))
                return

            prefix = ""
            for k in range(i):
                if i < len(lines[k]):
                    prefix += lines[k][i]
                else:
                    break
            # print prefix

            cands =prefix_m.get(prefix, [])
            
            for cand in cands:
                lines[i] = cand
                recur(i + 1, lines, sol)
        
        sol = []
        recur(0, [""] * n, sol)
        return sol

# Tricky, when to know we have found the solution. line 19
# Note that the same word can be used multiple times

# Tricky part
# How large can square go, max(map(len, words))
# prefix length < i, needs exact match
# How to terminate, if i > 0 and i == len(lines[0]):
# "" is also valid prefix to trigger the recursion running