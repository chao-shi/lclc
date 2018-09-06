"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        def append(head, tail, node):
            if tail == None:
                node.next, node.prev, node.child = None, None, None
                return node, node
            tail.next, node.prev, node.next, node.child = node, tail, None, None
            return head, node

        def recur(level_head, head, tail):
            p = level_head
            while p:
                p_next = p.next
                p_child = p.child
                head, tail = append(head, tail, p)
                if p_child:
                    head, tail = recur(p_child, head, tail)
                p = p_next
            return head, tail
        
        return recur(head, None, None)[0]
                
# Better than dummy nodes, dummy nodes we need to clear the link between dummy nodes and node 1.