class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        hm = {}
        wordDict = set(wordDict)
        def recur(s, i):
            if i == len(s):
                return [[]]
            elif i in hm:
                return hm[i]

            ret = []
            for j in range(i+1, len(s)+1):
                if s[i:j] in wordDict:
                    ret.extend([s[i:j]] + l for l in recur(s, j))
            hm[i] = ret
            return ret

        return [" ".join(l) for l in recur(s, 0)]

# This one shows one recursion is superior than DP for prefiltering problems. DP will have OJ TLE.