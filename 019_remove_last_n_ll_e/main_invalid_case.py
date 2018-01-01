# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dh = ListNode(-1)
        dh.next = head
        sp, fp = dh, dh
        i = 0
        while i < n+1 and fp:
            fp = fp.next
            i += 1
        
        if i < n + 1:
            # invalid case
            return None
            
        while fp:
            sp, fp = sp.next, fp.next
        sp.next = sp.next.next
        return dh.next

# 1. None node is n steps ahead of delete node
# 2. None node is n + 1 steps ahead of delete node parent
# 3. step 18 tries to initialize with n + 1 steps
# 4. invalid case if step cannot be n + 1