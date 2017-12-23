# Key idea
# What is the end of nested object: ']'
# What is the end of integer, a little harder, need to look one step ahead on digits
# Careful for the case of negative numbers
# Interesting thing is that no need to process comma in separate logic

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution(object):
    def deserialize(self, s):
        """
        :type s: str
        :rtype: NestedInteger
        """
        stack = [NestedInteger()]
        flag = 1

        for i in range(len(s)):
            ch = s[i]
            if ch == '[':
                stack.append(NestedInteger())
            
            elif ch == ']':
                top = stack.pop()
                stack[-1].add(top)
            
            elif ch == '-':
                flag = -1
            
            elif ch.isdigit():
                if stack and stack[-1].isInteger():
                    # Careful here, flag * int(ch)
                    stack[-1].setInteger(stack[-1].getInteger() * 10 + flag * int(ch))
                else:
                    stack.append(NestedInteger(flag * int(ch)))
                
                # End of integer
                if i == len(s) - 1 or not s[i+1].isdigit():
                    top = stack.pop()
                    stack[-1].add(top)
                    flag = 1
        
        return stack[-1].getList()[0]