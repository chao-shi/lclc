class ListNode(object):
    def __init__(self, val):
        self.prev, self.next, self.val = None, None, val

def remove(node):
    ret = node.prev
    node.prev.next = node.next
    if node.next:
        node.next.prev = node.prev
    node.prev, node.next = None, None
    return ret

class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        head = ListNode(-1)
        tail = head
        for ch in num:
            newtail = ListNode(ch)
            newtail.prev, tail.next = tail, newtail
            tail = newtail
        
        p = head.next
        for i in range(k):
            while p.next and p.val <= p.next.val:
                p = p.next
            p = remove(p)
        
        p = head.next
        ret = []
        while p:
            ret.append(p.val)
            p = p.next
        
        ret = "".join(ret).lstrip('0')
        if not ret:
            return '0'
        return ret

# Optimized code for main_naive.py. Use double linked list to improve remove element from the middle of array

# Line 8 when removing.