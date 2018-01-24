class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        maxv = 0
        for i, ch in enumerate(s):
            if ch == ')' and stack and s[stack[-1]] == '(':
                stack.pop()
                base = -1 if not stack else stack[-1]
                maxv = max(maxv, i - base)
            else:
                stack.append(i)
        return maxv
    
# Essential idea is line 12 how to understand base
# If ')' just popped an '(', then s[stack[-1]+1:i+1] should be all cleared,
# which forms a valid substring. If stack is empty, then this s[:i+1], which base = -1

# For things that cannot pop, go to line 15, we use this as a wall. ')' can be popped later
# ')' will be a permanant wall, which never pops

# Test case of )()())
# Stack growth
# [0]
# [0, 1]
# [0] check 2 - 0
# [0, 3] 
# [0], check 4 - 0
# [0, 5]

