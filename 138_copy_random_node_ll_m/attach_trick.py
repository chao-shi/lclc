# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        # Step 1 attach clone after each node
        p = head
        while p:
            np = RandomListNode(p.label)
            p.next, np.next = np, p.next
            p = p.next.next
        
        # Step 2 connet random
        p = head
        while p:
            if p.random:
                p.next.random = p.random.next
            p = p.next.next

        # Step 3: remove old node (Also important restore origin input)
        # E.G A - A' - B - B' - C - C'
        # p ends with C
        if not head:
            return None
        p, newhead = head, head.next
        while p.next:
            p.next, p = p.next.next, p.next
        return newhead

# Careful in step 3. (Need to restore origin input)

# If no need to recover input

        # # Step 3: remove old node (No )
        # if not head:
        #     return None
        # p = head.next
        # while p.next:
        #     p.next = p.next.next
        #     p = p.next
        # return head.next