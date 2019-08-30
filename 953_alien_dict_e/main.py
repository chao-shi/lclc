class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        def checkInOrder(w1, w2, order):
            for i in range(min(len(w1), len(w2))):
                if order[w1[i]] < order[w2[i]]:
                    return -1
                elif order[w1[i]] > order[w2[i]]:
                    return 1
                
            if len(w1) < len(w2):
                return -1
            elif len(w2) < len(w1):
                return 1
            else:
                return 0
            
        order = {ch: i for i, ch in enumerate(order)}
        for i in range(1, len(words)):
            if checkInOrder(words[i-1], words[i], order) == 1:
                return False
        return True