class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return []
        res = [[""]]
        for i in range(1, n+1):
            res.append(["(" + left + ")" + right for k in range(i) for left in res[k] for right in res[i-1-k]])
        return res[-1]