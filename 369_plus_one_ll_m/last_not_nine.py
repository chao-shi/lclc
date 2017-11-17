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
        lastNot9 = None

        while p:
            if p.val != 9:
                lastNot9 = p
            p = p.next
        
        lastNot9.val += 1
        p = lastNot9.next
        while p:
            p.val, p = 0, p.next
        
        if hd.val == 0:
            return hd.next
        else:
            return hd

# cleaner 