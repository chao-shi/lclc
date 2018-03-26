class MaxMap(object):
    def __init__(self):
        self.heap = []
        self.dict = {}
    
    # Need k because building may have same height
    def insert(self, k, v):
        tp = [-v, k, True]
        heapq.heappush(self.heap, tp)
        self.dict[k] = tp
    
    def remove(self, k):
        self.dict[k][2] = False
        del self.dict[k]
    
    def max_value(self):
        while self.heap and not self.heap[0][2]:
            heapq.heappop(self.heap)
        return -self.heap[0][0] if self.heap else None
        
class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        ts_map = {}
        for i, building in enumerate(buildings):
            start, end = building[0], building[1]
            ts_map.setdefault(start, (set(), set()))[0].add(i)
            ts_map.setdefault(end, (set(), set()))[1].add(i)
        
        actives = MaxMap()
        res = []
        for ts in sorted(ts_map.keys()):
            for b in ts_map[ts][0]:
                actives.insert(b, buildings[b][2])
            for b in ts_map[ts][1]:
                actives.remove(b)
            max_height = actives.max_value()
            
            # To accomodate generic data structure
            if max_height == None:
                max_height = 0

            # careful here
            if not res or res[-1][1] != max_height:
                res.append([ts, max_height])
        return res