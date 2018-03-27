class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack_push = []
        self.stack_pop = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.stack_push.append(x)
        

    def upside_down(self):
        if not self.stack_pop:
            while self.stack_push:
                self.stack_pop.append(self.stack_push.pop())

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        self.upside_down()
        if self.stack_pop:
            return self.stack_pop.pop()
        

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        self.upside_down()
        if self.stack_pop:
            return self.stack_pop[-1]
        
        

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.stack_pop) + len(self.stack_push) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()