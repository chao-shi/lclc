# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals = sorted(intervals, key=lambda intv: intv.start)
        res = []
        for intv in intervals:
            if res and res[-1].end >= intv.start:
                res[-1].end = max(intv.end, res[-1].end)
            else:
                res.append(intv)
        return res
        