"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, parent):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent
"""
class Solution(object):
    def inorderSuccessor(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if node.right:
            p = node.right
            while p.left:
                p = p.left
            return p
        else:
            while node.parent and node.parent.right == node:
                node = node.parent
            return node.parent