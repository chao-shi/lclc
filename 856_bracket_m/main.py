class Solution(object):
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        stack = [0]
        for i, ch in enumerate(S):
            if ch == ')' and S[i-1] == '(':
                stack.pop()
                stack[-1] += 1
            elif ch == ')':
                delta = 2 * stack.pop()
                stack[-1] += delta
            else:
                stack.append(0)
        return stack[-1]