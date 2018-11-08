from datetime import *

class LogSystem(object):

    def __init__(self):
        self.log_map = collections.defaultdict(set)
        self.ts_keys = []
        

    def to_ts(self, timestamp):
        y, m, d, h, mi, s = map(int, timestamp.split(":"))
        d = datetime(y, m, d, h, mi, s) - datetime(2000, 1, 1, 0, 0, 0)
        return int(d.total_seconds())
    
    def round_down_ts_gra(self, timestamp, gra):
        digits = [2000, 1, 1, 0, 0, 0]
        idx = ["Year", "Month", "Day", "Hour", "Minute", "Second"].index(gra)
        digits[:idx + 1] = map(int, timestamp.split(":"))[:idx + 1]
        d = datetime(*digits) - datetime(2000, 1, 1, 0, 0, 0)
        return int(d.total_seconds())

    def round_up_ts_gra(self, timestamp, gra):
        digits = [2000, 12, 31, 23, 59, 59]
        idx = ["Year", "Month", "Day", "Hour", "Minute", "Second"].index(gra)
        digits[:idx + 1] = map(int, timestamp.split(":"))[:idx + 1]
        
        # A little cubersome
        if digits[2] == 31:
            if digits[1] in set([4, 6, 9, 11]):
                digits[2] = 30
            elif digits[1] == 2:
                digits[2] = 28 if digits[0] % 4 != 0 else 29
                
        d = datetime(*digits) - datetime(2000, 1, 1, 0, 0, 0)
        return int(d.total_seconds())
    
    
    def put(self, id, timestamp):
        """
        :type id: int
        :type timestamp: str
        :rtype: void
        """
        ts = self.to_ts(timestamp)
        idx = bisect.bisect_left(self.ts_keys, ts)
        self.ts_keys.insert(idx, ts)
        self.log_map[ts].add(id)
        
    def retrieve(self, s, e, gra):
        """
        :type s: str
        :type e: str
        :type gra: str
        :rtype: List[int]
        """
        #print self.ts_keys, self.log_map
        st = self.round_down_ts_gra(s, gra)
        et = self.round_up_ts_gra(e, gra)
        #print st, et
        i = bisect.bisect_left(self.ts_keys, st)
        j = bisect.bisect_right(self.ts_keys, et)
        res = []
        for k in range(i, j):
            res.extend(self.log_map[self.ts_keys[k]])
        return res
        
    

# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(s,e,gra)