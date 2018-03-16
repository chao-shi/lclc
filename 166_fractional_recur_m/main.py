class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator * denominator < 0:
            return "-" + self.pos(abs(numerator), abs(denominator))
        return self.pos(abs(numerator), abs(denominator))

    def pos(self, numerator, denominator):
        def fraction(a, b):
            last_numerator = {}
            fractions = []
            while a > 0:
                if a in last_numerator:
                    idx = last_numerator[a]
                    ans = "."
                    ans += "".join(map(str, fractions[:idx]))
                    ans += "(" + "".join(map(str, fractions[idx:])) + ")"
                    return ans                
                last_numerator[a] = len(fractions)

                a *= 10
                q = a / b
                a %= b
                fractions.append(q)
            return "." + "".join(map(str, fractions))
        
        integer = numerator / denominator
        a, b = numerator % denominator, denominator
        ans = str(integer)
        if a != 0:
            ans += fraction(a, b)
        return ans

# Key idea keep the last appearance of numerator. (NOT NOT quotient)