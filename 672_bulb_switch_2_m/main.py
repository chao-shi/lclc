class Solution(object):
    def flipLights(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """      
        n = min(n, 3)
        if n == 0:
            return 1
        elif n == 1:
            m = min(m, 1)
            return [1, 2][m]
        elif n == 2:
            m = min(m, 2)
            return [1, 3, 4][m]
        else:
            m = min(m, 3)
            return [1, 4, 7, 8][m]
        
        # 111                 
        # 000 101 010 011
        # 111 101 010 100 000 001 110 
        # 000 001 010 011 100 101 110 011
        
        # 11
        # 00 10 01
        # 11 10 01 00
        
        # 1
        # 1 0