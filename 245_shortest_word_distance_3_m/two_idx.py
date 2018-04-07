class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        last1, last2 = None, None
        mindis = len(words)
        for i, word in enumerate(words):
            if word == word1 and last2 != None:
                mindis = min(mindis, i - last2)
            elif word == word2 and last1 != None:
                mindis = min(mindis, i - last1)
            
            if word == word1:
                last1 = i
            if word == word2:
                last2 = i
        return mindis