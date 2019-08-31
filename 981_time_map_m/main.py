class TimeMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.vmap = {}

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        self.vmap.setdefault(key, [])
        self.vmap[key].append((timestamp, value))
        

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        time_series = self.vmap.get(key, [])
        lb, hb = 0, len(time_series) - 1
        while lb <= hb:
            mid = (lb + hb) / 2
            if time_series[mid][0] == timestamp:
                return time_series[mid][1]
            elif time_series[mid][0] < timestamp:
                lb = mid + 1
            else:
                hb = mid - 1

        if hb == -1:
            # Careful
            # nothing matched found, 
            return ""
        else:
            return time_series[hb][1]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)