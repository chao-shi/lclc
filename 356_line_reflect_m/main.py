class Solution(object):
    def isReflected(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        if len(points) == 0:
            return True
        xs = [p[0] for p in points]
        x_mid = (min(xs) + max(xs)) / 2.0
        
        m = {}
        for p in points:
            dis = abs(p[0] - x_mid)
            # Don't care about those on the mirror
            ptr = (dis, p[1])
            if p[0] < x_mid:
                m[ptr] = m.get(ptr, 0) | 1
            elif p[0] > x_mid:
                m[ptr] = m.get(ptr, 0) | 2
        
        for ptr in m:
            if m[ptr] != 3:
                return False
        return True

# /2.0 to calculate the mid point