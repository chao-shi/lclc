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
        dh.next = head
        prev, p = dh, head
        while p:
            cnt = 0
            while p.next and p.next.val == p.val:
                p.next = p.next.next
                cnt += 1
            if cnt > 0:
                prev.next = p.next
            else:
                prev = p
            p = p.next
        return dh.next

# In place deletion