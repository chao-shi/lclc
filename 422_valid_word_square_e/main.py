class Solution(object):
    def validWordSquare(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        if len(words) != len(words[0]):
             return False
        for i, w in enumerate(words):
            col = "".join([ww[i] for ww in words if i < len(ww)])
            if w != col:
                return False
        return True