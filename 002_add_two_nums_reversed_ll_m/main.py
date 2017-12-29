# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dh = ListNode(-1)
        tail = dh
        
        c = 0
        while l1 or l2 or c:
            if l1:
                c += l1.val
            if l2:
                c += l2.val
            n = ListNode(c % 10)
            tail.next, tail = n, n
            c /= 10
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dh.next

# Possible optimization