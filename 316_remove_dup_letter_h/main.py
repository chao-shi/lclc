class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Last index map is useful, because as we iterate i from left to right
        # Easy to tell after i if there are still anything available for ch
        # check last_idx[ch] > i ?
        last_idx = {}
        for i, ch in enumerate(s):
            last_idx[ch] = i        
        
        in_stack = set()
        stack = []
        for i, ch in enumerate(s):
            if ch in in_stack:
                continue
            while stack and stack[-1] > ch and last_idx[stack[-1]] >= i:
                in_stack.remove(stack.pop())
            
            stack.append(ch)
            in_stack.add(ch)
        return "".join(stack)
    
# Use a stack to temporary hold the current optimal.
# Pop the top only if the top is bigger and still have something in the future.
        