class DoubleListNode(object):
    def __init__(self, k, v):
        self.key = k
        self.value = v
        self.prev, self.next = None, None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.head, self.tail = DoubleListNode(-1, -1), DoubleListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.hm = {}
        self.cache_size = 0
        self.capacity = capacity
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.hm:
            value = self.hm[key].value
            self.del_val(key)
            self.put_new_val(key, value)
            return value
        return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        self.del_val(key)
        self.put_new_val(key, value)
        self.adjust()
    
    def del_val(self, key):
        if key in self.hm:
            node = self.hm[key]
            node.next.prev, node.prev.next = node.prev, node.next
            del self.hm[key]
            self.cache_size -= 1
    
    def put_new_val(self, key, value):
        node = DoubleListNode(key, value)
        p = self.tail.prev
        p.next, node.next = node, self.tail
        self.tail.prev, node.prev = node, p
        self.hm[key] = node
        self.cache_size += 1
        
    def adjust(self):
        if self.cache_size > self.capacity:
            node = self.head.next
            key = node.key
            self.head.next, node.next.prev = node.next, self.head
            del self.hm[key]
            self.cache_size -= 1
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# obj = LRUCache(2)
# obj.put(1, 1)
# obj.put(2, 2)
# print(obj.get(1))
# obj.put(3, 3)
# print(obj.get(2))
# obj.put(4, 4)
# print(obj.get(1))
# print(obj.get(3))
# print(obj.get(4))

# # ["LRUCache","put","put","get","put","get","put","get","get","get"]
# # [[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]