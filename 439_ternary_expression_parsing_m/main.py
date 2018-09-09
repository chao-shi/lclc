class Solution(object):
    def parseTernary(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        
        def recur(i):
            if expression[i].isdigit():
                # Digit
                return expression[i], i + 1
            elif i == len(expression) - 1 or expression[i+1] != "?":
                # T/F leaf
                return expression[i], i + 1
            else:
                opt1, j = recur(i + 2)
                opt2, j = recur(j + 1)
                res = opt1 if expression[i] == 'T' else opt2
                return res, j
        
        return recur(0)[0]
    
# Block 15: Don't reuse the same i, might cause confusion