# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from Queue import PriorityQueue
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # This initialization is wrong
        # q = PriorityQueue([(head.val, head) for head in lists if head])
        
        q = PriorityQueue()
        for head in lists:
            if head:
                q.put((head.val, head))

        dh = ListNode(-1)
        tail = dh
        while not q.empty():
            v, n = q.get()
            tail.next, tail = n, n
            if n.next:
                q.put((n.next.val, n.next))
        return dh.next
        