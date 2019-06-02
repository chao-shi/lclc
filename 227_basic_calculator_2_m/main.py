import re
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.replace(" ", "")
        tokens = re.split("(\D+)", s)

        opr_stack, op_stack = [], []

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

        def eval_op_stack(next_op):
            while op_stack and (next_op == None or priority[op_stack[-1]] >= priority[next_op]):
                op = op_stack.pop()
                opr_stack.append(opt_map[op](opr_stack.pop(), opr_stack.pop()))
            op_stack.append(next_op)


        for i, t in enumerate(tokens):
            if i % 2 == 0:
                opr_stack.append(int(t))
            else:
                eval_op_stack(t)
               

        eval_op_stack(None)
        return opr_stack[-1]
    
# Change evalOps to take one parameter
# 
print Solution().calculate("3/2")