"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution(object):
    
    def mergeDoublyList(self, h1, h2):
        if h1 == None:
            return h2
        elif h2 == None:
            return h1
        else:
            t1, t2 = h1.left, h2.left
            h1.left, h2.left, t1.right, t2.right = t2, t1, h2, h1
            return h1
        
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None
        q1 = self.treeToDoublyList(root.left)
        q2 = self.treeToDoublyList(root.right)
        root.left, root.right = root, root
        
        h = self.mergeDoublyList(q1, root)
        h = self.mergeDoublyList(h, q2)
        return h