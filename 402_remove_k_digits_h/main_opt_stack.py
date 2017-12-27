class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack = []
        for ch in num:
            while k > 0 and stack and stack[-1] > ch:
                stack.pop()
                k -= 1
            stack.append(ch)
        
        # Think of \0 as char that pops everything remaining if still k > 0
        while k > 0:
            stack.pop()
            k -= 1

        ret = "".join(stack).lstrip('0')
        if not ret:
            return "0"
        return ret

# Careful of line 16

# Inspired by main_naive.py. Since everytime we always remove first element num[j] such that num[j] > num[j+1]
# a stack whch num[j+1] pops bigger element in the stack satisfy our purpose