class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        operands = []
        operators = {
            "+": lambda x, y: y + x,
            "-": lambda x, y: y - x,
            "*": lambda x, y: y * x,
            "/": lambda x, y: y / x if x * y >= 0 else -(abs(y)/abs(x)) 
        }
        for t in tokens:
            if t in operators:
                operands.append(operators[t](operands.pop(), operands.pop()))
            else:
                operands.append(int(t))
        return operands[0] if operands else None

# Stupid line 12 for Python negative division