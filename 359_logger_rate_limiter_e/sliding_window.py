# 169ms
class Logger(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # m is the message logged within (ts-10, ts] where ts is the last timestamp input
        # need m for quick look up
        # need q to clean up m
        self.m = set()
        self.q = collections.deque()
        

    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        while len(self.q):                                      # len
            ts, msg = self.q[0]                                 # access first one
            if ts <= timestamp - 10:                            # <= 
                self.m.remove(msg)                              # safe to remove, because same message can be logged only once in window
                self.q.popleft()                                # pop left
            else:
                break
        if message not in self.m:
            self.q.append([timestamp, message])
            self.m.add(message)
            return True
        return False

# Things not to do:
# 1. Iterate on timestamps in range [last_timestamp + 1, timestamp]

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
