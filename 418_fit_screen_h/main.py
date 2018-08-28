class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        s = " ".join(sentence) + " "
        l = len(s)

        # First char in line, its mapping index of the recuring pattern sentence
        i = 0
        for _ in range(rows):
            i += cols
            while i > 0 and s[i % l] != ' ':
                # Here we split some word into half.
                # Rewinding
                i -= 1
            i += 1
        return i/l

# i is a global index of infinite string 
# Sentence A_B_C, then the infinite string is
# A_B_C_A_B_C.....