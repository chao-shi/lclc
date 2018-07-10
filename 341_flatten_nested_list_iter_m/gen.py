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
        self.generator = self.gen()
        try:
            self.top = self.generator.next()
        except:
            self.top = None

    def recur(self, node):
        if node.isInteger():
            yield node.getInteger()
        else:
            for child in node.getList():
                for y in self.recur(child):
                    yield y

    def gen(self):
        for node in self.nl:
            for y in self.recur(node):
                yield y
        

    def next(self):
        """
        :rtype: int
        """
        val = self.top
        try:
            self.top = self.generator.next()
        except:
            self.top = None
        return val
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.top != None

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())