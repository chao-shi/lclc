class MyCircularDeque(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        :type k: int
        """
        self.arr = [None] * k
        self.cap = k
        self.size = 0
        self.h, self.t = 0, 0
        

    def insertFront(self, value):
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.size < self.cap:
            self.h = (self.h - 1 + self.cap) % self.cap
            self.arr[self.h] = value
            self.size += 1
            return True
        return False
        
        

    def insertLast(self, value):
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.size < self.cap:
            self.arr[self.t] = value
            self.t = (self.t + 1) % self.cap
            self.size += 1
            return True
        return False

    
    def deleteFront(self):
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if self.size > 0:
            self.h = (self.h + 1) % self.cap
            self.size -= 1
            return True
        return False
        

    def deleteLast(self):
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if self.size > 0:
            self.t = (self.t - 1 + self.cap) % self.cap
            self.size -= 1
            return True
        return False

    def getFront(self):
        """
        Get the front item from the deque.
        :rtype: int
        """
        if self.size > 0:
            return self.arr[self.h]
        return -1
        

    def getRear(self):
        """
        Get the last item from the deque.
        :rtype: int
        """
        if self.size > 0:
            idx = (self.t - 1 + self.cap) % self.cap
            return self.arr[idx]
        return -1
            
        

    def isEmpty(self):
        """
        Checks whether the circular deque is empty or not.
        :rtype: bool
        """
        return self.size == 0
        

    def isFull(self):
        """
        Checks whether the circular deque is full or not.
        :rtype: bool
        """
        return self.size == self.cap
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()