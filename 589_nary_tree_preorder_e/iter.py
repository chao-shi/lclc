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
        if not root:
            return []
        stack = [root]
        res = []
        
        while stack:
            top = stack.pop()
            res.append(top.val)
            for ch in top.children[::-1]:
                stack.append(ch)
        
        return res