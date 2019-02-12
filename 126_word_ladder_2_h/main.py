class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
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
        
        paths = [[beginWord]]
        
        while len(cands) > 0 and endWord not in cands:
            candsMap = {cand: [n for n in oneDiff(cand) if n in wordList] for cand in cands}
            paths = [path + [n] for path in paths for n in candsMap[path[-1]]]
            cands = set(cand for v in candsMap.values() for cand in v)
            for cand in cands:
                wordList.remove(cand)
        
        return [path for path in paths if path[-1] == endWord]
    
# Very brilliant idea by me

# Good to keeps the cands structure for BFS, and keep other computation result as metadata on the side
# line 25 computes the mapping between previous cands and next cands