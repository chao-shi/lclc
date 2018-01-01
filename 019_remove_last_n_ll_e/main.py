# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dh = ListNode(-1)
        dh.next = head
        sp, fp = dh, dh
        for i in range(n+1):
            fp = fp.next
        while fp:
            sp, fp = sp.next, fp.next
        sp.next = sp.next.next
        return dh.next