# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class SummaryRanges(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.intervals = []

    def addNum(self, val):
        """
        :type val: int
        :rtype: void
        """
        def firstBad(intervals, f):
            li, hi = 0, len(intervals) - 1
            while li <= hi:
                mid = (li + hi) / 2
                if f(intervals[mid]):
                    hi = mid - 1
                else:
                    li = mid + 1
            return li

        newInterval = Interval(val, val)
        intervals = self.intervals
        i = firstBad(intervals, lambda intv: intv.end >= newInterval.start - 1)
        j = firstBad(intervals, lambda intv: intv.start > newInterval.end + 1)
        
        # [i, j) needs to be rewritten
        mergedStart = newInterval.start if i == len(intervals) else min(intervals[i].start, newInterval.start)
        mergedEnd = newInterval.end if j == 0 else max(intervals[j-1].end, newInterval.end)

        self.intervals = intervals[:i] + [Interval(mergedStart, mergedEnd)] + intervals[j:]
        

    def getIntervals(self):
        """
        :rtype: List[Interval]
        """
        return self.intervals

# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()


# Copy from insert interval question
# What is difference
# In insert interval question, [2, 2] and [3, 3] cannot be merged (float based)
# Here we need to merge them

# The difference is that line 32 and line 33 needs to change.

# Don't use UNION FIND, too much memory, needs to store every element in the stream