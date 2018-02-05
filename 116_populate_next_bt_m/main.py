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
        def recur(root):
            if not root:
                return
            if root.left:
                root.left.next = root.right
                recur(root.left)
            if root.right:
                if root.next:
                    root.right.next = root.next.left
                recur(root.right)
        
        recur(root)