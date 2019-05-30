class Solution(object):
    def parseTernary(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        stack = []
        for i in range(len(expression) - 1, -1, -1):
            if expression[i].isdigit():
                # operand
                stack.append(expression[i])
            elif expression[i].isalpha() and (i == len(expression) - 1 or expression[i+1] == ":"):
                # operand
                stack.append(expression[i])
            elif expression[i].isalpha():
                oper1, oper2 = stack.pop(), stack.pop()
                stack.append(oper1 if expression[i] == 'T' else oper2)
        return stack[-1]

print Solution().parseTernary("T?2:3")