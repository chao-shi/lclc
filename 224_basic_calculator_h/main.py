class Tokenizer(object):
    def __init__(self, s):
        self.s = s.replace(" ", "")
        self.i = 0

    def nextToken(self):
        if self.i == len(self.s):
            return None

        sign = 1
        cur = self.i

        # How to parse negative number
        if self.s[self.i] == "-":
            if self.i == 0 or self.s[self.i - 1] == "(":
                sign = -1
                cur += 1
        
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
            "-": lambda x, y : y - x
        }

        def evalOps():
            while operators and operators[-1] in "+-":
                opt = operators.pop()
                operands.append(opt_map[opt](operands.pop(), operands.pop()))

        while True:
            token = tokenizer.nextToken()
            if token == None:
                break
            elif isinstance(token, int):
                operands.append(token)
            elif token in "+-":
                evalOps()
                operators.append(token)
            elif token == "(":
                operators.append(token)
            else:
                evalOps()
                operators.pop()
        
        # Don't forget the end
        evalOps()
        return operands[-1]
    
# 1. Negative number is token by himself
# 2. A generator like tokenizer
# 3. No need to convert to postfix explicitly
# 4. evalOps is a good function. It takes one operator, two operands and push back one operand
# 5. Don't forget the closing on line 69