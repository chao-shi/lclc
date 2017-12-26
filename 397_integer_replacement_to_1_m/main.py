class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        cands = set([n])
        step = 0
        while 1 not in cands:
            newcands = set()
            for c in cands:
                if c % 2 == 0:
                    newcands.add(c/2)
                else:
                    newcands.add(c - 1)
                    newcands.add(c + 1)
            cands = newcands
            step += 1
        return step