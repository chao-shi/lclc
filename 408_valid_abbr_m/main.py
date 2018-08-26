class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        i, j = 0, 0
        while i < len(word) and j < len(abbr):
            jj = j
            while jj < len(abbr) and abbr[jj].isdigit():
                jj += 1
            
            if jj > j and abbr[j] != '0':
                occur = int(abbr[j:jj])
                # handle i out of range outside
                i, j = i + occur, jj
            elif word[i] != abbr[j]:
                return False
            else:
                i, j = i + 1, j + 1
        
        return i == len(word) and j == len(abbr)
                
# Case of "a", "01" and "word", "w0ord" handled by line 14 abbr[j] != '0'