class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        stack = []
        for ch in S:
            if ch == "(":
                stack.append(ch)
            else:
                if stack and stack[-1] == "(":
                    stack.pop()
                else:
                    stack.append(")")
        return len(stack)