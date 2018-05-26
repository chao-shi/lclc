class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        # len
        self.hmax, self.hmin = [], []

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        if not self.hmax or num <= -self.hmax[0]:
            heapq.heappush(self.hmax, -num)
        else:
            heapq.heappush(self.hmin, num)
        
        if len(self.hmax) - len(self.hmin) == 2:
            heapq.heappush(self.hmin, -heapq.heappop(self.hmax))
        elif len(self.hmax) - len(self.hmin) == -1:
            heapq.heappush(self.hmax, -heapq.heappop(self.hmin))

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.hmax) + len(self.hmin) == 0:
            return None
        elif (len(self.hmax) + len(self.hmin)) % 2 == 0:
            return (-self.hmax[0] + self.hmin[0]) / 2.0
        else:
            return -self.hmax[0]
            

# Line 15 empty case

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()