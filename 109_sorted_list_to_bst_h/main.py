# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        def length(head):
            cnt = 0
            while head:
                cnt += 1
                head = head.next
            return cnt
        
        def recur(head, n):
            if n == 0:
                # careful about second ret arg
                return None, head
            left, head = recur(head, n/2)
            root = TreeNode(head.val)
            right, head = recur(head.next, n - n/2 - 1)
            root.left, root.right = left, right
            return root, head

        n = length(head)
        root, _ = recur(head, n)
        return root