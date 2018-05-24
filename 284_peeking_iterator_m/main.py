# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator(object):
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iter = iterator
        self.top = None
        if self.iter.hasNext():
            self.top = self.iter.next()

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        value = self.top
        if value == None:
            raise Exception("No more items")
        return value
        

    def next(self):
        """
        :rtype: int
        """
        value = self.top
        if value == None:
            raise Exception("No more items")

        if self.iter.hasNext():
            self.top = self.iter.next()
        else:
            self.top = None
        return value

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.top != None

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].