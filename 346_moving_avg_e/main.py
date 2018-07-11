class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.win = collections.deque()
        self.size = size
        self.sum = 0

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.win.append(val)
        self.sum += val
        if len(self.win) > self.size:
            head = self.win.popleft()
            self.sum -= head
        return float(self.sum) / len(self.win)
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)