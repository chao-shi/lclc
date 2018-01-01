# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dh = ListNode(-1)
        dt = dh
        p1, p2 = l1, l2
        while p1 or p2:
            if not p1 or (p2 and p1.val > p2.val):
                dt.next, dt = p2, p2
                p2 = p2.next
            else:
                dt.next, dt = p1, p1
                p1 = p1.next
        return dh.next