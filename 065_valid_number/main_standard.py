class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()
        int_pattern = "(0|-?[1-9][0-9]*)"
        frac_pattern = "(\\.[0-9]+)"
        exp_pattern = "(e-?[1-9][0-9]*)"
        pattern = "^({}{}?){}?$".format(int_pattern, frac_pattern, exp_pattern)
        m = re.match(pattern, s)
        return m != None

# Standard format, does not pass OJ