class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.vec = vec2d
        self.i, self.j = 0, -1
        self.moveNext()

    def next(self):
        """
        :rtype: int
        """
        ret = self.vec[self.i][self.j]
        self.moveNext()
        return ret
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.i < len(self.vec)
        
    def moveNext(self):
        self.j += 1
        while self.i < len(self.vec) and self.j == len(self.vec[self.i]):
            self.i += 1
            self.j = 0

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())

# My solution is better. A lot of answers online are assuming each hasNext call is with one next call after