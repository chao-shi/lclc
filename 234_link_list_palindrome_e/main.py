# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fp, sp = head, head
        while fp:
            fp = fp.next
            if fp:
                fp, sp = fp.next, sp.next
        
        prev, p = None, sp
        while p:
            p.next, prev, p = prev, p, p.next
        h2 = prev
        
        while h2 and h2.val == head.val:
            h2, head = h2.next, head.next
        return h2 == None