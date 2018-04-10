# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        delta = {}
        for intv in intervals:
            delta[intv.start] = delta.get(intv.start, 0) + 1
            delta[intv.end] = delta.get(intv.end, 0) - 1
        
        active = 0
        maxroom = 0
        for ts in sorted(delta.keys()):
            active += delta[ts]
            maxroom = max(maxroom, active)
        return maxroom