class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = [0]
        while len(res) < num + 1:
            res = res + map(lambda x : x + 1, res)
        return res[:num + 1]

# If from n to m, we will need to look at n and start with some iteration approach