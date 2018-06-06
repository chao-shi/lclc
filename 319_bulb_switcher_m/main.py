class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        # C(n) = C(n-1) + sigma_1_to_n (1 if n mod i == 0 else 0) % 2
        # The second term is only 1 if n is square number
        
        return int(math.sqrt(n)) 