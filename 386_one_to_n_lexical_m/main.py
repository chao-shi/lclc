# Recursion did not pass OJ
# DFS careful when root is zero, 

class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = []
        def recur(root):
            if root > n:
                return
            if root != 0:
                res.append(root)
            nexts = range(10) if root != 0 else range(1, 10)
            for i in nexts:
                recur(root * 10 + i)
        recur(0)
        return res