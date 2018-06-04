class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        res = [[""]]
        for ch in word:
            new_res = []
            for r in res:
                new_res.append(r + [ch])
                if r and isinstance(r[-1], int):
                    new_res.append(r[:len(r) - 1] + [r[-1] + 1])
                else:
                    new_res.append(r + [1])
            res = new_res
        return ["".join(map(str, r)) for r in res]