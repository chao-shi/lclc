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
        if not head or not head.next:
            # When part of the list can be empty. easier to pick separately
            return

        sprev, sp, fp = None, head, head
        while fp:
            fp = fp.next
            if fp:
                fp = fp.next
                sprev, sp = sp, sp.next

        # sp is starting of second half
        # 1, 2, 3 sp is 2
        # 1, 2, 3, 4, sp is 3
        
        # L1 break
        sprev.next = None

        # Reverse list 2
        p, prev = sp, None
        while p:
            p.next, prev, p = prev, p, p.next

        h2 = prev
        h1 = head

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

# line 17 block, sp stays at the end of link list 1
# fp stops at the last element of link list
# best way to get middle point