class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack=[]

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        minv = self.getMin()
        newminv = x if minv == None else min(minv, x)
        self.stack.append((x, newminv))
        

    def pop(self):
        """
        :rtype: void
        """
        if self.stack:
            x, minv = self.stack.pop()
            return x
        

    def top(self):
        """
        :rtype: int
        """
        if self.stack:
            x, minv = self.stack[-1]
            return x

    def getMin(self):
        """
        :rtype: int
        """
        if self.stack:
            x, minv = self.stack[-1]
            return minv


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# Note that min(None, 0) is None, None is smaller than all numbers