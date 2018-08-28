class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        k = 0
        cnt_sent = 0
        
        # To opt, add memory table for repeating patterns
        mt = {}

        for i in range(rows):            
            j = 0
            while j + len(sentence[k]) <= cols:
                j += len(sentence[k]) + 1
                if k == len(sentence) - 1:
                    cnt_sent += 1
                k = (k + 1) % len(sentence)
            
            # OPT
            mt[i] = cnt_sent
            if k == 0:
                break
        
        cycle = len(mt.keys())
        cnt_sent *= rows / cycle
        if rows % cycle > 0:
            cnt_sent += mt[rows % cycle - 1]
        return cnt_sent