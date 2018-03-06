class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        hm = {}
        wordDict = set(wordDict)
        def recur(s, i):
            if i == len(s):
                return True
            elif i in hm:
                return hm[i]

            for j in range(i+1, len(s)+1):
                if s[i:j] in wordDict and recur(s, j):
                    hm[i] = True
                    return True
            hm[i] = False
            return False

        return recur(s, 0)