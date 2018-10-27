# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution(object):
    def outerTrees(self, points):
        """
        :type points: List[Point]
        :rtype: List[Point]
        """
        # Use cross product
        # to check if p1 is on left of p2
        # If same direction, return if longer, then we populate the between points
        
        # I started with to see if shorter. Does not work for [[1,2],[2,2],[4,2]], exit prematurely at point [2, 2]
        def on_left_or_longer(p1, p2, p_base):
            v1, v2 = (p1.x - p_base.x, p1.y - p_base.y), (p2.x - p_base.x, p2.y - p_base.y)
            cross_p = v1[0] * v2[1] - v1[1] * v2[0]
            if cross_p < 0:
                return True
            elif cross_p == 0:
                return v1[0] ** 2 + v1[1] ** 2 > v2[0] ** 2 + v2[1] ** 2
            else:
                return False
        
        def in_between(p1, p2, p3):
            #print p1.x, p2.x, p3.x
            v1, v2 = (p2.x - p1.x, p2.y - p1.y), (p3.x - p1.x, p3.y - p1.y)
            inner_p = v1[0]  * v2[0] + v1[1] * v2[1]
            d1 = v1[0] ** 2 + v1[1] ** 2
            d2 = v2[0] ** 2 + v2[1] ** 2
            return inner_p ** 2 == d1 * d2

        H0 = min((p.x, i) for i, p in enumerate(points))[1]
        H = set([H0])
        i = H0

        while True: 
            left_most_j = None
            for j in range(len(points)):
                if j != i and (left_most_j == None or on_left_or_longer(points[j], points[left_most_j], points[i])):
                    left_most_j = j
            
            if left_most_j == None:
                break
            
            # Handle in between points separately
            for j in range(len(points)):
                if j != left_most_j and j != i and in_between(points[i], points[j], points[left_most_j]):
                    H.add(j)
            
            if left_most_j != H0:
                H.add(left_most_j)
                i = left_most_j
            else:
                break
        
        return map(lambda x:points[x], H)
    
# Convex hull problem, but minor difference is do we need to count all numbers on the line.
# Not very clean though to handle colinear