"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next):
        self.val = val
        self.next = next
"""
class Solution(object):
    def insert(self, head, insertVal):
        """
        :type head: Node
        :type insertVal: int
        :rtype: Node
        """
        if not head:
            return Node(insertVal)
        p = head
        while not (p.val <= insertVal and p.next.val >= insertVal):
            if p.next.val < p.val < insertVal: 
                break
            elif insertVal < p.next.val < p.val:
                break
            elif p.next == head:
                break
            p = p.next
        # insert at p
        n = Node(insertVal)
        p.next, n.next = n, p.next
        return head
    
# 3->4->1