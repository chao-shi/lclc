# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dh = ListNode(None)
        tail = dh
        prev, p = None, head
        while p:
            if (prev and prev.val == p.val) or (p.next and p.next.val == p.val):
                prev, p = p, p.next
            else:
                tail.next, tail = p, p
                prev, p = p, p.next
                tail.next = None
        return dh.next

# Don't forget tail.next = None