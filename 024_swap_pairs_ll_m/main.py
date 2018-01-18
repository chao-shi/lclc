# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dh = ListNode(-1)
        tail = dh
        p = head
        while p:
            q = p.next
            if q:
                tail.next, q.next, p.next, tail, p = q, p, None, p, q.next
            else:
                tail.next, tail, p = p, p, None
        return dh.next
            