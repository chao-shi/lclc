class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        alphas = [chr(i) for i in range(ord('a'), ord('z') + 1)]
        wordList = set(wordList)

        def oneDiff(word):
            return [word[:i] + ch + word[i+1:] for i in range(len(word)) for ch in alphas if ch != word[i]]
        
        # Only first round some cands may not be in wordList
        cands = set([beginWord])
        
        # One corner case
        if beginWord == endWord and endWord not in wordList:
            return False
        
        step = 1
        
        while len(cands) > 0 and endWord not in cands:
            cands = set(n for cand in cands for n in oneDiff(cand) if n in wordList)
            for cand in cands:
                wordList.remove(cand)
            step += 1
        
        if len(cands) == 0:
            return 0
        return step

# Best approach. 

# Some other posts in LC is suggesting building a map for the wordList with wild card
# The result looks like
# "c*g" => [cog, cig]
# "_og" => [cog, fog]

# This is only slightly faster in look up (no need to look up all 26 letters). But it is significantly slower in building
# In building. The loop will be K * N where K is the average length of word. This uses a lot of storage

# The lazy look up approach is much faster in case of shorter ladders

