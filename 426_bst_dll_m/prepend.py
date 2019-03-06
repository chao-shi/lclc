"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution(object):
        
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        self.head = None

        def recur(root):
            if not root:
                return
            recur(root.right)
            left_child = root.left
            if self.head:
                root.left, root.right = self.head.left, self.head
                self.head.left = root
                # Don't forget here, update tail !!!!
                root.left.right = root
            else:
                root.left, root.right = root, root
            self.head = root
            recur(left_child)
        
        recur(root)
        return self.head