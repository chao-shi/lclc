"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        self.res = []
        def recur(root):
            if root:
                self.res.append(root.val)
                for ch in root.children:
                    recur(ch)
        
        recur(root)
        return self.res