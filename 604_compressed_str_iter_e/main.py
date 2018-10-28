class StringIterator(object):

    def __init__(self, compressedString):
        """
        :type compressedString: str
        """
        self.alphas = re.findall("\D", compressedString)
        self.reps = map(int, re.findall("\d+", compressedString))
        self.idx = 0
        self.cnt = self.reps[0] if self.reps else None

    def next(self):
        """
        :rtype: str
        """
        if not self.hasNext():
            return " "

        val = self.alphas[self.idx]
        self.cnt -= 1
        if self.cnt == 0:
            self.idx += 1
            if self.idx < len(self.reps):
                self.cnt = self.reps[self.idx]
        return val        
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.idx < len(self.alphas)


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()