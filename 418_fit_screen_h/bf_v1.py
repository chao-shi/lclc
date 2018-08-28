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
        for i in range(rows):
            j = 0
            while j + len(sentence[k]) <= cols:
                j += len(sentence[k]) + 1
                if k == len(sentence) - 1:
                    cnt_sent += 1
                k = (k + 1) % len(sentence)
        return cnt_sent
        