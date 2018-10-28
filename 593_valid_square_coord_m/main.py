class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        def dis(p, q):
            return (p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2
        
        def perpend(p1, p2, p3):
            v1, v2 = (p2[0] - p1[0], p2[1] - p1[1]), (p3[0] - p2[0], p3[1] - p2[1])
            return v1[0] * v2[0] + v1[1] * v2[1] == 0
        
        # This will gurantee p1 p4 and p2 p3 are across diagonal.
        p1, p2, p3, p4 = sorted([p1, p2, p3, p4])
        
        # Check Rhombus
        ds = set([dis(p1, p2), dis(p2, p4), dis(p4, p3), dis(p3, p1)])
        
        # Check rectangle
        angles = set([perpend(p1, p2, p4), perpend(p2, p4, p3), perpend(p4, p3, p1), perpend(p3, p1, p2)])
        
        return len(ds) == 1 and len(angles) == 1 and angles.pop() == True and ds.pop() > 0
        