class ListNode(object):
    def __init__(self, v, f):
        self.prev, self.next = None, None
        self.f, self.v = f, v


class DDL(object):
    def __init__(self):
        self.head, self.tail = None, None


    def append(self, node):
        if not self.tail:
            node.prev, node.next = None, None
            self.head, self.tail = node, node
        else:
            self.tail.next, node.prev, node.next = node, self.tail, None
            self.tail = node


    def pop(self):
        if self.tail == None:
            return None

        ret = self.tail
        self.tail = ret.prev

        ret.prev = None
        if self.tail != None:
            self.tail.next = None
        else:
            self.tail, self.head = None, None
        return ret


    def insert_before(self, c, node):
        if not c:
            # Tail
            self.append(node)
        elif c.prev == None:
            # Head
            c.prev, node.next = node, c
            self.head = node
        else:
            # Middle
            a = c.prev
            a.next, node.next, node.prev, c.prev = node, c, a, node


    def remove(self, node):
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next

        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev


class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        self.ddl = DDL()
        self.key_map = {}
        self.most_recent_map = {}
        
        self.val_map = {}


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.key_map:
            return -1
        else:
            self.touch(key)
            return self.val_map[key]


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        # special case for cap = 0, no space even after removing
        if self.cap == 0:
            return

        if len(self.key_map) == self.cap and not key in self.key_map:
            key_evict = self.removeLF()
            del self.val_map[key_evict]
        
        self.touch(key)
        self.val_map[key] = value
        

    # touch is to increment the frequent and last_timestamp
    # All function below only handle key, not value
    def touch(self, key):
        freq = self.key_map[key].f if key in self.key_map else 0

        # Very concise here, work for freq = 0 also
        insert_before = self.most_recent_map.get(freq + 1, None)
        if not insert_before:
            insert_before = self.most_recent_map.get(freq, None)


        cur_node = self.key_map.get(key, None)
        new_node = ListNode(key, freq + 1)

        # Important !!
        # insert, first then delete old
        # Could be insert_before is cur_node
        self.ddl.insert_before(insert_before, new_node)
        if cur_node:
            self.removeNode(cur_node)
        
        self.most_recent_map[freq + 1] = new_node
        self.key_map[key] = new_node
    

    def removeNode(self, node):
        key, freq = node.v, node.f
        if self.most_recent_map[freq] == node:
            if node.next != None and node.next.f == freq:
                self.most_recent_map[freq] = node.next
            else:
                del self.most_recent_map[freq]

        del self.key_map[key]
        self.ddl.remove(node)


    def removeLF(self):
        ln = self.ddl.pop()
        key, freq = ln.v, ln.f
        del self.key_map[key]
        if self.most_recent_map[freq] == ln:
            del self.most_recent_map[freq]
        return key
            
        
# most_recent_map has key of frequency, mapping to a node in ddl
# ddl is sorted by freq DESC, then timestamp DESC.
# So most recent is on the left most for the segment of same freq.
        
# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# The trick is all about how to find the insertion point when touching an element. 
# Block 111.
# To update the frequency, we need to insert first then delete
# 
# TODO (How to abstract as linked hash set)