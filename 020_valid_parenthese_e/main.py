class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        match = {')': '(', ']': '[', '}': '{'}
        for ch in s:
            if ch in match and (not stack or stack[-1] != match[ch]):
                return False
            if ch in match:
                stack.pop()
            else:
                stack.append(ch)
        return len(stack) == 0