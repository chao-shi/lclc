"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []
        level = [root]
        ret = []
        while level:
            ret.append([n.val for n in level])
            level = [c for n in level for c in n.children]
        return ret