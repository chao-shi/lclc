class WordDistance(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.words = words
        self.idx_map = {}
        for i, word in enumerate(words):
            self.idx_map.setdefault(word, []).append(i)

    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        l1, l2 = self.idx_map[word1], self.idx_map[word2]
        mindis = len(self.words)
        
        i, j = 0, 0
        while i < len(l1) and j < len(l2):
            mindis = min(mindis, abs(l1[i] - l2[j]))
            if l1[i] < l2[j]:
                i += 1
            else:
                j += 1
        return mindis
                


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)