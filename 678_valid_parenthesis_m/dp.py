class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        mt = [[False] * (n + 1) for _ in range(n+1)]
        
        for i in range(n+1):
            mt[i][i] = True
            
        for i in range(n):
            if s[i] == "*":
                mt[i][i+1] = True

        for diff in range(2, n + 1):
            for i in range(n - diff + 1):
                j = i + diff
                if s[i] == ')' or s[j-1] == '(':
                    continue
                elif mt[i+1][j-1]:
                    mt[i][j] = True
                else:
                    for k in range(i+1, j-1):
                        if s[k] in "(*" and mt[i][k] and mt[k+1][j-1]:
                            mt[i][j] = True
                            break
        return mt[0][n]
    
# * can be empty