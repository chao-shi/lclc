# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
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

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.nl = nestedList
        self.pos = -1
        self.stack = []
        self.next_val = self.seekValue()
    
    # Seek next Integer
    def seekValue(self):
        
        while True:
            node = self.seekNode()
            if node == None:
                return None
            elif node.isInteger():
                return node.getInteger()

    # Seek next Node, return None if reach end
    def seekNode(self):
        if self.stack:
            node = self.stack.pop()
            if not node.isInteger():
                for child in node.getList()[::-1]:
                    self.stack.append(child)
        
        # Separate if block here
        if not self.stack:
            self.pos += 1
            if len(self.nl) > self.pos:
                self.stack.append(self.nl[self.pos])
        return self.stack[-1] if self.stack else None

    def next(self):
        """
        :rtype: int
        """
        val = self.next_val
        self.next_val = self.seekValue()
        return val


    def hasNext(self):
        """
        :rtype: bool
        """
        return self.next_val != None

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

# Don't confuse, this is not the left_stack in_order iteration, this is PRE-ORDER
# Much simpler, think about how we did in BST for pre-order