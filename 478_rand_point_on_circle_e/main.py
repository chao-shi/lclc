class Solution(object):

    def __init__(self, radius, x_center, y_center):
        """
        :type radius: float
        :type x_center: float
        :type y_center: float
        """
        self.r = radius
        self.x = x_center
        self.y = y_center
        

    def randPoint(self):
        """
        :rtype: List[float]
        """
        # R is triangular distribution 
        # Think about thing ring area, which is linear to distance from center
        # thena is uniform
        
        # Third param is peak point
        r = random.triangular(0, self.r, self.r) 
        theta = random.uniform(-math.pi, math.pi)
        return [self.x + r * math.cos(theta), self.y + r * math.sin(theta)]


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()