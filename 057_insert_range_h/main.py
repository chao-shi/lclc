# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
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

        i = firstBad(intervals, lambda intv: intv.end >= newInterval.start)
        j = firstBad(intervals, lambda intv: intv.start > newInterval.end)
        
        # [i, j) needs to be rewritten
        mergedStart = newInterval.start if i == len(intervals) else min(intervals[i].start, newInterval.start)
        mergedEnd = newInterval.end if j == 0 else max(intervals[j-1].end, newInterval.end)

        return intervals[:i] + [Interval(mergedStart, mergedEnd)] + intervals[j:]