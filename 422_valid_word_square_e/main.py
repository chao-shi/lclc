class Solution(object):
    def validWordSquare(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        for i, w in enumerate(words):
            column = ""
            for j in range(len(words)):
                if i < len(words[j]):
                    column += words[j][i]
                else:
                    column += " "
            
            if column[:len(w)] != w:
                return False

            # checking trailing spaces, here for sure len(column) >= len(w)
            if any(ch != " " for ch in column[len(w):]):
                return False
            
        return True