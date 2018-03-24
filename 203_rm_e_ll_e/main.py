# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dh = ListNode(-1)
        tail = dh
        while head:
            if head.val != val:
                tail.next, tail = head, head
            head = head.next
            tail.next = None
        return dh.next
    
# Line 20 terminating tail is essential in this case