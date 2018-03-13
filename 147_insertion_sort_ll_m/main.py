# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dh = ListNode(-1)
        while head:
            prev, p = dh, dh.next
            while p and p.val < head.val:
                prev, p = p, p.next
            prev.next, head.next, head = head, p, head.next
        return dh.next
            
        