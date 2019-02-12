# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        sp, fp = head, head
        meet = None
        while fp and fp.next and fp.next.next:
            fp = fp.next.next
            sp = sp.next
            
            if sp == fp:
                meet = sp
                break
        
        if not meet:
            return None
        
        sp, fp = head, meet
        while sp != fp:
            sp = sp.next
            fp = fp.next
        return sp
                