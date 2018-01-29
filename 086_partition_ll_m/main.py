# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        dh1, dh2 = ListNode(None), ListNode(None)
        tail1, tail2 = dh1, dh2
        p = head
        while p:
            if p.val < x:
                tail1.next, p.next, tail1, p = p, None, p, p.next
            else:
                tail2.next, p.next, tail2, p = p, None, p, p.next
        tail1.next = dh2.next
        return dh1.next