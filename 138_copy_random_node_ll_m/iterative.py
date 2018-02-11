# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        hm = {}
        dh = RandomListNode(-1)
        tail = dh
        
        p = head
        while p:
            np = RandomListNode(p.label)
            tail.next, tail = np, np
            hm[p] = np
            p = p.next
        
        p = head
        while p:
            if p.random:
                hm[p].random = hm[p.random]
            p = p.next

        return dh.next

# slightly faster than recursion