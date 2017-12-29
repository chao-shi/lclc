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
        c = 0
        p1, p2 = l1, l2
        dh = ListNode(-1)
        dt = dh

        while p1 or p2 or c:
            #early termination
            if not p1 and c == 0:
                dt.next = p2
                break
            elif not p2 and c == 0:
                dt.next = p1
                break
            
            if p1:
                c += p1.val
            if p2:
                c += p2.val
            node = ListNode(c%10)
            dt.next, dt = node, node
            c = c / 10
            
            if p1:
                p1 = p1.next
            if p2:
                p2 = p2.next

        return dh.next