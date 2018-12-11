class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        stack = []
        sum = 0
        for op in ops:
            if op == "C":
                last = stack.pop()
                sum -= last
            elif op == "D":
                score = stack[-1] * 2
                stack.append(score)
                sum += score
            elif op == "+":
                score = stack[-2] + stack[-1]
                stack.append(score)
                sum += score
            else:
                stack.append(int(op))
                sum += int(op)
        return sum