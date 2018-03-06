# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head:
            # mid point not valid for empty list
            return

        sp, fp = head, head
        while fp:
            fp = fp.next
            if fp:
                fp, sp = fp.next, sp.next
        
        h1, h2 = head, sp.next
        # link list break
        sp.next = None

        # Reverse list 2
        p, prev = h2, None
        while p:
            p.next, prev, p = prev, p, p.next
        h2 = prev

        dh = ListNode(-1)
        tail = dh
        while h1 or h2:
            if h1:
                tail.next, tail, h1 = h1, h1, h1.next
            if h2:
                tail.next, tail, h2 = h2, h2, h2.next
                
# 1. Don't return anything because head won't change
# 2. Line 25 important, don't forget to BREAK the list
# 3. mid point approach does not work for empty list