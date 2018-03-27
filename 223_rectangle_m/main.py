class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        s1 = abs(A - C) * abs(B - D)
        s2 = abs(E - G) * abs(F - H)
        total = s1 + s2

        left, right = max(A, E), min(C, G)
        top, bottom = min(D, H), max(B, F)
        
        if left < right and bottom < top:
            total -= (right - left) * (top - bottom)
        return total
            