class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        # "" is never valid, even though "" = "" + "", the questions says both shorter
        # tricky base case
        def checkConcat(w, i, word_set):
            # The below is wrong
            # if i == len(w) and i > 0:
            #     return True
            if 0 < i < len(w) and w[i:] in word_set:
                return True
            for j in range(i + 1, len(w)):
                w1 = w[i:j]
                if w1 in word_set and checkConcat(w, j, word_set):
                    return True
            return False
        
        words = sorted(words, key=lambda x:len(x))
        word_set = set()
        res = []

        for w in words:
            if checkConcat(w, 0, word_set):
                res.append(w)
            word_set.add(w)
        return res
    
# Key optimization: sort the words by length !!!
#
#
# To optimize 
# 1. Store i in memory table. Case of abcd | ... where after | does not make concat
#    and word_set = ["a", "bcd", "ab", "cd"], so no need to recompute
# 2. the checkConcat function can input another TrieNode node so that we don't need to recheck for each w1