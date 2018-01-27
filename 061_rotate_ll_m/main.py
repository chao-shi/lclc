# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        length = 0
        prev, p = None, head
        while p:
            prev, p, length = p, p.next, length + 1
        
        if length == 0:
            return head

        # circulate the ll
        prev.next = head
        
        # ll shift to right, header moves left
        k %= length
        k = (length - k) % length
        for i in range(k):
            prev, head = head, head.next
        prev.next = None
        return head

# Careful about line 28, need one more mod