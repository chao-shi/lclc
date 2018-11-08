class Solution(object):
    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        """
        def accu(term):
            # Normalize
            if term[0] != "-":
                term = "+" + term
            term = term.replace("+x", "+1x").replace("-x", "-1x")

            x_f = re.findall("[-+]\d+x", term)
            a_f = re.findall("[-+]\d+", term)
            print term, x_f, a_f
            x_sum = sum([int(e[:len(e) - 1]) for e in x_f])
            a_sum = sum(map(int, a_f))
            n_sum = a_sum - x_sum
            return x_sum, n_sum
        
        l, r = equation.split("=")
        lx, ln = accu(l)
        rx, rn = accu(r)
        
        fx, fn = lx - rx, rn - ln
        if fx != 0:
            return "x={}".format(fn / fx)
        elif fn == 0:
            return "Infinite solutions"
        else:
            return "No solution"