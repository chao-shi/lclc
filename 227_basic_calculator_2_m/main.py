class Tokenizer(object):
    def __init__(self, s):
        self.s = s.replace(" ", "")
        self.i = 0

    def nextToken(self):
        if self.i == len(self.s):
            return None

        sign = 1
        cur = self.i
        
        num = 0
        while cur < len(self.s) and self.s[cur].isdigit():
            num = num * 10 + int(self.s[cur])
            cur += 1
        
        if cur > self.i:
            self.i = cur
            return sign * num
        else:
            ret = self.s[self.i]
            self.i += 1
            return ret
            
        
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        tokenizer = Tokenizer(s)
        operands = []
        operators = []

        opt_map = {
            "+": lambda x, y : x + y,
            "-": lambda x, y : y - x,
            "*": lambda x, y : x * y,
            "/": lambda x, y : y / x
        }
        
        priority = {
            "+": 0, 
            "-": 0,
            "*": 1,
            "/": 1
        }

        def evalOps(op):
            while operators and (op == None or priority[operators[-1]] >= priority[op]):
                opt = operators.pop()
                operands.append(opt_map[opt](operands.pop(), operands.pop()))

        while True:
            token = tokenizer.nextToken()
            if token == None:
                break
            elif isinstance(token, int):
                operands.append(token)
            else:
                evalOps(token)
                operators.append(token)
        
        # Don't forget the end
        evalOps(None)
        return operands[-1]
    
# Change evalOps to take one parameter