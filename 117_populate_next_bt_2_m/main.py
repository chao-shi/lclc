# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        p = root
        while p:
            dh = TreeLinkNode(1)
            tail = dh
            while p:
                if p.left:
                    tail.next, tail = p.left, p.left
                if p.right:
                    tail.next, tail = p.right, p.right
                p = p.next
            p = dh.next