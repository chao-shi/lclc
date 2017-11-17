# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        hd = ListNode(0)
        hd.next = head
        
        p = hd
        while p:
            q = p.next
            while q and q.val == 9:
                q = q.next
            if not q:
                p.val += 1
                p = p.next
                while p:
                    p.val, p = 0, p.next
            else:
                p = q
        
        if hd.val == 0:
            return hd.next
        else:
            return hd

# Loop invariant:
# p starts at the place where IT IS NOT 9.
# skip all 9 and end up at q
# if q is the end of the list, then p is the one to increment, and all after that reset to 0
# otherwise p moves to q