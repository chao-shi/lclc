class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        self.ids = set()
        ans = []
        map = {}

        for i in range(len(positions)):
            pos = positions[i]

            minid = i + 1

            for v in [[0,1],[1,0],[0,-1],[-1,0]]:
                xx, yy = pos[0] + v[0], pos[1] + v[1]
                if (xx, yy) in map:
                    minid = min(minid, map[(xx, yy)])
            
            self.ids.add(minid)

            for v in [[0,1],[1,0],[0,-1],[-1,0]]:
                xx, yy = pos[0] + v[0], pos[1] + v[1]
                if (xx, yy) in map and map[(xx, yy)] > minid and map[(xx, yy)] in self.ids:
                    self.ids.remove(map[(xx, yy)])
            
            self.span(pos[0], pos[1], m, n, map, minid)
            
            ans.append(len(self.ids))
        
        return ans
                        
    def span(self, x, y, m, n, map, id):
        map[(x, y)] = id
        
        for v in [[0,1],[1,0],[0,-1],[-1,0]]:
            xx, yy = x + v[0], y + v[1]
            if (xx, yy) in map and map[(xx, yy)] != id:
                self.span(xx, yy, m, n, map, id)
        