# The queue will have tuple 
# (freq, ts, value, gc)

class PQ(object):

    def __init__(self):
        self.q = []
        self.q_map = {}


    def add(self, v, p, ts):
        if v in self.q_map:
            self.remove(v)
        node = [p, ts, v, True]
        heapq.heappush(self.q, node)
        self.q_map[v] = node


    def touch(self, v, ts):
        p = 0
        if v in self.q_map:
            p =self.q_map[v][0]
        self.add(v, p + 1, ts)

        
    def remove(self, v):
        self.q_map.pop(v)[-1] = False

    
    def contains(self, v):
        return v in self.q_map

    
    def pop(self):
        while self.q:
            node = heapq.heappop(self.q)
            if node[-1]:
                del self.q_map[node[2]]
                return node[:3]
        return None


    def size(self):
        return len(self.q_map)


class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        self.key_pq = PQ()
        self.val_map = {}
        self.counter = itertools.count()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        ts = next(self.counter)

        if not self.key_pq.contains(key):
            return -1

        self.key_pq.touch(key, ts)
        return self.val_map.get(key)
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        ts = next(self.counter)
        
        # A little nasty to handle, because we cannot insert blindly
        if self.cap == 0:
            return 

        if self.key_pq.size() == self.cap and not self.key_pq.contains(key):
            evict_key = self.key_pq.pop()[-1]
            del self.val_map[evict_key]

        self.key_pq.touch(key, ts)
        self.val_map[key] = value
            
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# 
# Not O(1) though.