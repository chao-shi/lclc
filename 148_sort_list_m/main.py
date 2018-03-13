# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def recur(head):
            if not head or not head.next:
                return head

            sp, fp = head, head
            while fp and fp.next:
                fp = fp.next.next
                if fp:
                    sp = sp.next

            h1, h2, sp.next = head, sp.next, None
            h1 = recur(h1)
            h2 = recur(h2)
            return merge(h1, h2)
        
        def merge(h1, h2):
            dh = ListNode(-1)
            tail = dh
            while h1 or h2:
                if not h2 or (h1 and h1.val <= h2.val):
                    tail.next, tail, h1 = h1, h1, h1.next
                else:
                    tail.next, tail, h2 = h2, h2, h2.next
            return dh.next
        
        return recur(head)

# Careful about base case