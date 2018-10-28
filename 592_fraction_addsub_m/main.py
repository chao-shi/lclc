class Solution(object):
    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        def lcd(n1, n2):
            if n1 == 0 or n2 == 0:
                return 0
            n1, n2 = max(n1, n2), min(n2, n1)
            while True:
                if n1 % n2 == 0:
                    return n2
                n1, n2 = n2, n1 % n2
        
        def lcm(n1, n2):
            cd = lcd(n1, n2)
            return (n1 * n2) / cd
        
        # So smart answer from forum. 
        # Sign goes to numerator
        ints = map(int, re.findall('[+-]?\d+', expression))
        
        N, D = 0, 1
        for i in range(0, len(ints), 2):
            n, d = ints[i:i+2]
            cm = lcm(D, d)
            N, D = N * cm / D + n * cm / d, cm
            
            if N != 0:
                # careful
                cd = lcd(D, abs(N))
                D /= cd
                N /= cd
            else:
                # careful
                D = 1
        return "{}/{}".format(N, D)
        

# Few things
# 1. Line 22 extract very efficient
# 2. fraction reduce. Careful when nominator is zero or negative.