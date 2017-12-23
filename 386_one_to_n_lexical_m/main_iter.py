class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = []
        num = 1
        for i in range(n):
            res.append(num)
            if num * 10 <= n:
                num *= 10
            else:
                while num == n or num % 10 == 9:
                    # while num is at the edge of tree, needs backtracing
                    num /= 10
                num += 1
        return res