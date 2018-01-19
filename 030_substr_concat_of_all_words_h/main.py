class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        wordbag = collections.Counter(words)
        res = []
        k = len(words[0])
        for d in range(k):
            i = d
            bag = {}
            matchedlen = 0
            for j in range(d + k, len(s) + 1, k):
                wordin = s[j-k:j]
                bag[wordin] = bag.get(wordin, 0) + 1
                if bag[wordin] <= wordbag.get(wordin):
                    matchedlen += k
                if j - i > k * len(words):
                    wordout = s[i:i+k]
                    bag[wordout] = bag[wordout] - 1
                    if bag[wordout] < wordbag.get(wordout):
                        matchedlen -= k
                    i += k
                if matchedlen == k * len(words):
                    res.append(i)
        return res

# line 15
# bag keep count of all words in the window, matchedlen is updated accordingly 
# This solution is good because wordbag is generic, it handles all cases even if word seen is
# not part of the dictionary (see line 18 and line 23)