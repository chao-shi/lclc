class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.vs = [v1, v2]
        self.ps = [0, 0]
        self.i = 0 if len(v1) > 0 else 1
        

    def next(self):
        """
        :rtype: int
        """
        if not self.hasNext():
            raise Exception("Iteration exception")
        value = self.vs[self.i][self.ps[self.i]]
        self.moveNext()
        return value

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.ps[self.i] < len(self.vs[self.i])
    
    def moveNext(self):
        self.ps[self.i] += 1
        # Move to another list if possible
        if self.ps[1 - self.i] < len(self.vs[1 - self.i]):
            self.i = 1 - self.i
        

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())