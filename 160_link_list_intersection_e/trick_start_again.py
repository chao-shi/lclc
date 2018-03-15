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
        self.crossA, self.crossB = True, True

        def moveA(n):
            if n:
                return n.next
            elif self.crossA:
                self.crossA = False
                return headB

        def moveB(n):
            if n:
                return n.next
            elif self.crossB:
                self.crossB = False
                return headA
        
        pA, pB = headA, headB
        while pA != pB:
            pA, pB = moveA(pA), moveB(pB)
        return pA