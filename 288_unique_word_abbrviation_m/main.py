class ValidWordAbbr(object):

    def __init__(self, dictionary):
        """
        :type dictionary: List[str]
        """
        self.dict = {}
        for word in dictionary:
            ab = self.abbr(word)
            self.dict.setdefault(ab, word)
            if self.dict[ab] != word:
                self.dict[ab] = False

    def isUnique(self, word):
        """
        :type word: str
        :rtype: bool
        """
        ab = self.abbr(word)
        return ab not in self.dict or self.dict[ab] == word

    
    def abbr(self, word):
        if len(word) <= 2:
            return word
        return word[0] + str(len(word) - 2) + word[-1]


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)

# Careful, case of dictionary = [deer] and word = deer, should return True
# A simple presence check of abbreviation does not work.