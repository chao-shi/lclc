class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # lower bound and higher bound of "(" in stack
        lb, hb = 0, 0
        for i, ch in enumerate(s):
            if ch == '(':
                lb, hb = lb + 1, hb + 1
            elif ch == ')':
                if hb < 1:
                    return False
                lb, hb = max(0, lb - 1), hb - 1
            else:
                lb, hb = max(0, lb - 1), hb + 1
        return lb == 0

# Good greedy approach