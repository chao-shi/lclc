class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()
        int_pattern = "(\\d+)"
        frac_pattern = "(\.\\d+)"
        exp_pattern = "(e(\+|-)?\\d+)"
        pattern = "^(\+|-)?({}{}?|{}\.|{}){}?$".format(int_pattern, frac_pattern, int_pattern, frac_pattern, exp_pattern)
        m = re.match(pattern, s)
        return m != None

# Wierd cases: 01, .1, 3. +.8
# Confusing question