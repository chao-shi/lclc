class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        m = {ch:i for i, line in enumerate(["qwertyuiop", "asdfghjkl", "zxcvbnm"]) for ch in line}
        res = []
        for w in words:
            r = set([m[ch.lower()] for ch in w])
            if len(r) == 1:
                res.append(w)
        return res