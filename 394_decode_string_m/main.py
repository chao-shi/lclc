class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        mulstack = []
        strstack = [[]]
        for i, ch in enumerate(s):
            if ch.isdigit():
                if i > 0 and s[i-1].isdigit():
                    mulstack[-1] = mulstack[-1] * 10 + int(ch)
                else:
                    mulstack.append(int(ch))
            elif ch.isalpha():
                strstack[-1].append(ch)
            elif ch == '[':
                strstack.append([])
            else:
                s = strstack.pop()
                mul = mulstack.pop()
                strstack[-1].extend(s * mul)
        return "".join(strstack[-1])

# Key idea. 
# each time we encounter '[': Push something on top of stack
# each time we encounter ']': pop something from stack and merge it with the new stack
# the multiplier needs to be in a new stack
# We assume [abc] is invalid, so no need to process when multiplier is 1