# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dh1, dh2 = ListNode(-1), ListNode(-1)
        t1, t2 = dh1, dh2
        
        p = head
        while p:
            pn = p.next
            t1.next, p.next, t1 = p, None, p
            t2.next, t2 = pn, pn
            
            if pn:
                p = pn.next
            else:
                p = None
        
        t1.next = dh2.next
        return dh1.next
            