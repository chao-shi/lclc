class MyCircularQueue(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        self.head, self.tail = 0, 0
        self.arr = [None] * k
        self.k = k
        self.size = 0

    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if not self.isFull():
            self.arr[self.tail] = value
            self.tail = (self.tail + 1) % self.k
            self.size += 1
            return True
        else:
            return False
        
        

    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        if not self.isEmpty():
            self.head = (self.head + 1) % self.k
            self.size -= 1
            return True
        else:
            return False

    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        if not self.isEmpty():
            return self.arr[self.head]
        else:
            return -1
        

    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        if not self.isEmpty():
            idx = (self.tail + self.k - 1) % self.k
            return self.arr[idx]
        else:
            return -1
        

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        return self.size == 0

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        return self.size == self.k
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()