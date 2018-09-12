# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1, l2 = self.reverse(l1), self.reverse(l2)
        p1, p2 = l1, l2
        c = 0
        h, t = None, None
        while p1 or p2:
            v = c
            if p1:
                v += p1.val
                p1 = p1.next
            if p2:
                v += p2.val
                p2 = p2.next
            
            n=ListNode(v%10)
            
            if h == None:
                h, t = n, n
            else:
                t.next, t = n, n
            
            c = v/10
        
        if c > 0:
            n = ListNode(1)
            t.next, t = n, n

        return self.reverse(h)

    def reverse(self, l):
        h = None
        p = l
        while p != None:
            p.next, h , p = h, p, p.next
        return h

# Crappy question, no good solution. Some solution convert the ll to stack/deque.
# Nothing great about that.