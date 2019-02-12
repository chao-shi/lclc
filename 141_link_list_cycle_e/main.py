# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fp, sp = head, head
        while fp and fp.next and fp.next.next:
            fp = fp.next.next
            sp = sp.next
            if fp == sp:
                return True
        return False

# Linear list fp will never be same as sp after one operation in line 20
# so logic 20 is solid