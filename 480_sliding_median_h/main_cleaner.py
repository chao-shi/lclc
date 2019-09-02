class PQ(object):

    def __init__(self):
        self.q = []
        self.q_map = {}


    def add(self, v, p):
        if v in self.q_map:
            self.remove(v)
        node = [p, v, True]
        heapq.heappush(self.q, node)
        self.q_map[v] = node


    def remove(self, v):
        self.q_map.pop(v)[-1] = False

    # Pop value
    def pop(self):
        while self.q:
            node = heapq.heappop(self.q)
            if node[-1]:
                del self.q_map[node[1]]
                return node[:2]
        return None


    def first(self):
        while self.q and not self.q[0][-1]:
            heapq.heappop(self.q)
        return self.q[0][:2] if self.q else None


    def size(self):
        return len(self.q_map)
    
    def contains(self, v):
        return v in self.q_map


# Good here, idx is the value and num is the priority
# Idx is the unique value
class MedianCalculator(object):
    def __init__(self):
        self.hmin, self.hmax = PQ(), PQ()
        
    def add_num(self, idx, num):
        # This is wrong, can't blindly add to hmin
        # self.hmin.add(idx, num)
        if self.hmax.size() == 0 or -self.hmax.first()[0] > num:
            self.hmax.add(idx, -num)
        else:
            self.hmin.add(idx, num)
        self.rebalance()
            
    def del_num(self, idx, num):
        if self.hmin.contains(idx):
            self.hmin.remove(idx)
        elif self.hmax.contains(idx):
            self.hmax.remove(idx)
        self.rebalance()
        
    def rebalance(self):
        while not 0 <= self.hmax.size() - self.hmin.size() <= 1:
            if self.hmax.size() - self.hmin.size() > 1:
                num, idx = self.hmax.pop()
                self.hmin.add(idx, -num)
            elif self.hmax.size() - self.hmin.size() < 0:
                num, idx = self.hmin.pop()
                self.hmax.add(idx, -num)

    def get_median(self):
        if self.hmax.size() == 0:
            return None
        elif self.hmax.size() > self.hmin.size():
            return float(-self.hmax.first()[0])
        else:
            return (-self.hmax.first()[0] + self.hmin.first()[0]) / 2.0

            
class Solution(object):
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        mc = MedianCalculator()
        res = []
        for i in range(len(nums)):
            # print i, mc.hmax.q, mc.hmax.q_map, mc.hmin.q, mc.hmin.q_map
            mc.add_num(i, nums[i])
            # print i, mc.hmax.q, mc.hmax.q_map, mc.hmin.q, mc.hmin.q_map
            if i - k >= 0:
                mc.del_num(i - k, nums[i-k])
            if i >= k - 1:
                res.append(mc.get_median())
        return res

# Careful on line 52