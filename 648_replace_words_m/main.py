class Solution(object):
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        dictionary = set(dict)
        res = []
        for w in sentence.split():
            is_successor = False
            for i in range(1, len(w)):
                if w[:i] in dictionary:
                    res.append(w[:i])
                    is_successor = True
                    break

            if not is_successor:
                res.append(w)
        return " ".join(res)