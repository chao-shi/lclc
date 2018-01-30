class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if not len(s1) + len(s2) == len(s3):
            return False

        cands = set([(0, 0)])
        for k in range(1, len(s3) + 1):
            newcands = set()
            for cand in cands:
                if cand[0] < len(s1) and s1[cand[0]] == s3[k-1]:
                    newcands.add((cand[0] + 1, cand[1]))
                if cand[1] < len(s2) and s2[cand[1]] == s3[k-1]:
                    newcands.add((cand[0], cand[1] + 1))
            cands = newcands
        return len(cands) > 0
            