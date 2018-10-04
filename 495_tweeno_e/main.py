class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        total_duration = 0
        wake_up = 0
        for p in timeSeries:
            total_duration += p + duration - max(wake_up, p)
            wake_up = p + duration
        return total_duration