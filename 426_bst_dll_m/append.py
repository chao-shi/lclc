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
            recur(root.left)
            right_child = root.right
            if self.head:
                root.left, root.right = self.head.left, self.head
                self.head.left = root
                # Don't forget here, update tail !!!!
                root.left.right = root
            else:
                self.head = root
                root.left, root.right = root, root
            recur(right_child)
        
        recur(root)
        return self.head
    
# append also works