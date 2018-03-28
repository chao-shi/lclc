class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        # \d is digit, \D is [^0-9]
        # brackets means include splitter in the result
        tokens = re.split("(\D)", input)
        nums = map(int, tokens[::2])
        ops = tokens[1::2]
        
        func_map = {
            "+": lambda x, y : x + y,
            "-": lambda x, y : x - y,
            "*": lambda x, y : x * y,
            "/": lambda x, y : x / y
        }

        def recur(li, hi):
            if li == hi:
                return [nums[li]]
            ret = []
            for i in range(li, hi):
                for v1 in recur(li, i):
                    for v2 in recur(i + 1, hi):
                        ret.append(func_map[ops[i]](v1, v2))
            return ret
        
        return recur(0, len(ops))
    
# Good approach how to preprocess token here