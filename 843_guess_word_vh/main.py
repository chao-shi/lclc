# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Master(object):
#    def guess(self, word):
#        """
#        :type word: str
#        :rtype int
#        """

class Solution(object):
    def findSecretWord(self, wordlist, master):
        """
        :type wordlist: List[Str]
        :type master: Master
        :rtype: None
        """
        n = len(wordlist[0])
        while True:
            cand = self.selectCand(wordlist)
            print cand, wordlist
            cnt = master.guess(cand)
            if cnt == n:
                break
            else:
                wordlist = self.filterCands(wordlist, cand, cnt)
            
            
    def filterCands(self, wordList, lastGuess, matched):
        return filter(lambda w: self.countMatched(w, lastGuess) == matched, wordList)


    def countMatched(self, w, target):
        return sum(0 if w[i] != target[i] else 1 for i in range(len(w)))
    
    
    def selectCand(self, wordList):
        best_worst = len(wordList) + 1
        for cand in wordList:
            match_cnt_map = collections.defaultdict(int)
            for w in wordList:
                matched = self.countMatched(cand, w)
                match_cnt_map[matched] += 1
            worst_match_cnt = max(match_cnt_map.values())
            if worst_match_cnt < best_worst:
                best_worst = worst_match_cnt
                best_cand = cand
        return best_cand