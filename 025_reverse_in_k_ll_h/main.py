# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dh = ListNode(-1)
        tail = dh
        p = head
        while p:
            tmpp = p
            i, prev = 0, None
            while i < k and p:
                p.next, prev, p = prev, p, p.next
                i += 1
            
            if i == k:
                tail.next, tail = prev, tmpp
            else:
                pp, prev = prev, None
                while pp:
                    pp.next, prev, pp = prev, pp, pp.next
                tail.next = prev
        
        return dh.next
            
        