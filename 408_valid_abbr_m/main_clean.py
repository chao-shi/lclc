class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        abbr = re.split("(\d+)", abbr)
        
        j = 0
        for ab in abbr:
            if ab.isdigit():
                if ab[0] == '0':
                    return False
                j += int(ab)
                if j > len(word):
                    return False
            elif word[j:j+len(ab)] != ab:
                return False
            else:
                j += len(ab)
        return j == len(word)

# Careful about line 13, specific to this question