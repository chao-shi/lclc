# stack stores the length of the parent folders

class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        stack = []
        maxlen = 0
        for line in input.split('\n'):
            ident = line.count('\t')
            while len(stack) > ident:
                stack.pop()
            filename = line.replace('\t', '')
            stack.append(len(filename))
            if '.' in filename:
                maxlen = max(maxlen, sum(stack) + len(stack) - 1)
        return maxlen