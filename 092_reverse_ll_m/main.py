# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dh = ListNode(None)
        dh.next = head
        p = dh
        for i in range(m-1):
            p = p.next
        tail = p

        p = p.next
        for i in range(n - m):
            # Can check p and p.next for overflow
            new_first = p.next
            first = tail.next
            tail.next, new_first.next, p.next = new_first, first, p.next.next
        return dh.next
    
# The idea is twisting pairs, good thing is this keeps the ll also in good shape
# Start from line 22
# case of 1,2,3,4,5  2 4
# L = 1, 2, 3, 4, 5   p = 2
# L = 1, 3, 2, 4, 5   p = 2
# L = 1, 4, 3, 2, 5   p = 2
# P never moves