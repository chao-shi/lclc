class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        last_idx = {}
        mindis = len(words)
        for i, word in enumerate(words):
            if word == word1 and word2 in last_idx:
                mindis = min(mindis, i - last_idx[word2])
            elif word == word2 and word1 in last_idx:
                mindis = min(mindis, i - last_idx[word1])
            last_idx[word] = i
        return mindis