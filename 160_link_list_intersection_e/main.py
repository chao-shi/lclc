# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        def len(head):
            cnt = 0
            while head:
                cnt += 1
                head = head.next
            return cnt
        
        len1, len2 = len(headA), len(headB)
        
        sp, fp = (headA, headB) if len1 < len2 else (headB, headA)
        
        for i in range(abs(len1 - len2)):
            fp = fp.next
        
        while sp != fp:
            sp, fp = sp.next, fp.next
        return sp
# Brackets needed for line 22