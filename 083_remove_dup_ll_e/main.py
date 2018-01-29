# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dh = ListNode(None)
        tail = dh
        p = head
        while p:
            if p.val != tail.val:
                tail.next, p.next, tail, p = p, None, p, p.next
            else:
                p = p.next
        return dh.next