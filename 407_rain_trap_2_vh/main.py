class UnionFind(object):
    def __init__(self, values):
        self.parent = {v : v for v in values}
        self.size = {v:1 for v in values}
        self.set_cnt = len(values)
    
    def add(self, u):
        self.parent[u] = u
        self.size[u] = 1
        self.set_cnt += 1
    
    def has(self, u):
        return u in self.parent

    def root(self, u):
        while u != self.parent[u]:
            self.parent[u] = self.parent[self.parent[u]]
            u = self.parent[u]
        return u
        
    def find(self, u, v):
        return self.root(u) == self.root(v)
    
    def union(self, u, v):
        ru, rv = self.root(u), self.root(v)
        # Important, don't want to double the tree size
        if ru == rv:
            return 
        if self.size[ru] > self.size[rv]:
            self.parent[rv] = ru
            self.size[ru] += self.size[rv]
        else:
            self.parent[ru] = rv
            self.size[rv] += self.size[ru]
        self.set_cnt -= 1


class WaterCounter(object):
    def __init__(self, m, n):
        self.m, self.n = m, n
        self.ut = UnionFind([(-1, -1)])
        
    def addWater(self, x, y):
        self.ut.add((x, y))
        for v in [(0, 1), (0, -1), (1, 0) ,(-1, 0)]:
            xx, yy = x + v[0], y + v[1]
            if xx < 0 or xx == self.m or yy < 0 or yy == self.n:
                self.ut.union((x, y), (-1, -1))
            elif self.ut.has((xx, yy)):
                # Neighbor is water also
                self.ut.union((x, y), (xx, yy))

    def countOcean(self):
        ocean_root = self.ut.root((-1, -1))
        return self.ut.size[ocean_root] - 1
    
    def countLake(self):
        return len(self.ut.parent) - 1 - self.countOcean()


class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        if not heightMap:
            return 0

        m, n = len(heightMap), len(heightMap[0])
        hm = [[i, j, heightMap[i][j]] for i in range(m) for j in range(n)]
        hm = sorted(hm, key=lambda x:x[2])
        
        wm = WaterCounter(m, n)
        volume = 0
        
        i = 0
        while i < len(hm):
            j = i + 1
            while j < len(hm) and hm[j][2] == hm[j-1][2]:
                j += 1
            
            # last round can be ignored
            if j == len(hm):
                break
            
            # hm[i:j] are currently on the surface,
            # will be under water next round
            water_line = hm[j][2]
            last_water_line = hm[i][2]

            for k in range(i, j):
                wm.addWater(hm[k][0], hm[k][1])
            
            volume += (water_line - last_water_line) * wm.countLake()
            
            # print hm[i:j], water_line, last_water_line, wm.countLake(), wm.ut.parent
            i = j
        
        return volume
    
# How it works. The water goes up, Title turns from hill to water. Water join lake to ocean and join lake between
# each other too. The key idea is to count the number of lakes using union find algorithm.

# Sort the tiles by height. 
# height[i:j] are the same height, the current water level is height[i][2]
# which will be sumerged by next water level height[j][2]

# Add all tiles in height[i:j] to water. Do a union function if the neighbor is a water as well. 
# If neighbor is out of boundary, do a union with ocean (-1, -1)