class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        wordDict = set(wordDict)
        m = [False] * (len(s) + 1)
        m[0] = True
        for i in range(1, len(s) + 1):
            for j in range(i):
                if s[j:i] in wordDict and m[j]:
                    m[i] = True
                    break
        return m[len(s)]
        