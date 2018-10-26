class Solution(object):
    def minDistance(self, height, width, tree, squirrel, nuts):
        """
        :type height: int
        :type width: int
        :type tree: List[int]
        :type squirrel: List[int]
        :type nuts: List[List[int]]
        :rtype: int
        """
        def dis(x1, y1, x2, y2):
            return abs(x1 - x2) + abs(y1-y2)
        
        distance = []
        min_d = None
        sum_d1 = 0
        for nut in nuts:
            d1 = dis(nut[0], nut[1], tree[0], tree[1])
            d2 = dis(nut[0], nut[1], squirrel[0], squirrel[1])
            distance.append((d1, d2))
            if min_d == None or d2 - d1 < min_d:
                min_d = d2 - d1
            sum_d1 += d1
                
        return 2 * sum_d1 + min_d
            
            
# (A, B) where A is distance to tree and B is distance to S
# suppose we pick 0 first
# Answer will be 2A1 + 2A2 + ..... + A0 + B0
# which is 2(A0 + A1 + ....) + B0 - A0
# Just need to minimize B - A